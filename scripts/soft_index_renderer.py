import math, os
from PIL import Image, ImageDraw, ImageFilter, ImageChops

S, SS = 1024, 4
W = S * SS
OUT = os.path.dirname(os.path.abspath(__file__))

INK    = (62, 52, 46, 248)      # warm umber, never pure black
STROKE = 0.0248

# ---------------- geometry ----------------
def squircle(n=4.6, steps=1440):
    p = []
    for i in range(steps):
        t = 2*math.pi*i/steps; c, s = math.cos(t), math.sin(t)
        p.append((0.5+0.5*math.copysign(abs(c)**(2.0/n), c),
                  0.5+0.5*math.copysign(abs(s)**(2.0/n), s)))
    return p

def arc(cx, cy, r, a0, a1, steps=None):
    steps = steps or max(10, int(abs(a1-a0)/(math.pi/90)))
    return [(cx+r*math.cos(a0+(a1-a0)*i/steps), cy+r*math.sin(a0+(a1-a0)*i/steps))
            for i in range(steps+1)]

def circle(cx, cy, r, steps=240):
    return [(cx+r*math.cos(2*math.pi*i/steps), cy+r*math.sin(2*math.pi*i/steps))
            for i in range(steps)]

def seg(p0, p1, steps=30):
    return [(p0[0]+(p1[0]-p0[0])*i/steps, p0[1]+(p1[1]-p0[1])*i/steps) for i in range(steps+1)]

def bez(p0, p1, p2, p3, steps=70):
    o = []
    for i in range(steps+1):
        t = i/steps; u = 1-t
        o.append((u**3*p0[0]+3*u*u*t*p1[0]+3*u*t*t*p2[0]+t**3*p3[0],
                  u**3*p0[1]+3*u*u*t*p1[1]+3*u*t*t*p2[1]+t**3*p3[1]))
    return o

def rrect(x, y, w, h, r):
    x2, y2 = x+w, y+h
    return (seg((x+r, y), (x2-r, y)) + arc(x2-r, y+r, r, -math.pi/2, 0)
          + seg((x2, y+r), (x2, y2-r)) + arc(x2-r, y2-r, r, 0, math.pi/2)
          + seg((x2-r, y2), (x+r, y2)) + arc(x+r, y2-r, r, math.pi/2, math.pi)
          + seg((x, y2-r), (x, y+r)) + arc(x+r, y+r, r, math.pi, 1.5*math.pi))

def sparkle(cx, cy, r, pinch=0.32):
    tips = [(cx, cy-r), (cx+r, cy), (cx, cy+r), (cx-r, cy)]
    p = []
    for i in range(4):
        a, b = tips[i], tips[(i+1) % 4]
        c1 = (a[0]+(cx-a[0])*(1-pinch), a[1]+(cy-a[1])*(1-pinch))
        c2 = (b[0]+(cx-b[0])*(1-pinch), b[1]+(cy-b[1])*(1-pinch))
        p += bez(a, c1, c2, b, 30)[:-1]
    return p

# ---------------- the hand: slow, not jittery ----------------
def soften(pts, closed, amp, seed):
    """Low-frequency only (k=1,2,3). High harmonics are what made the lines look cracked."""
    K = (1, 2, 3)
    ph = [((seed*53 + j*149) % 197)/197.0*2*math.pi for j in range(len(K))]
    n = len(pts); out = []
    for i, (px, py) in enumerate(pts):
        a = pts[(i-1) % n] if closed else pts[max(i-1, 0)]
        b = pts[(i+1) % n] if closed else pts[min(i+1, n-1)]
        dx, dy = b[0]-a[0], b[1]-a[1]; L = math.hypot(dx, dy) or 1e-9
        t = i/n if closed else i/(n-1)
        d = sum(math.sin(2*math.pi*K[j]*t + ph[j])/(j+1.4) for j in range(len(K)))
        if not closed:
            d *= math.sin(math.pi*t)**0.5
        out.append((px - dy/L*amp*d, py + dx/L*amp*d))
    return out

class Sheet:
    def __init__(self, bg):
        self.img  = bg
        self.wash  = Image.new("RGBA", (W, W), (0, 0, 0, 0))
        self.shade = Image.new("RGBA", (W, W), (0, 0, 0, 0))
        self.ink   = Image.new("RGBA", (W, W), (0, 0, 0, 0))
        self.wd  = ImageDraw.Draw(self.wash)
        self.sd  = ImageDraw.Draw(self.shade)
        self.idr = ImageDraw.Draw(self.ink)
        self.shadow = (118, 94, 76, 64)

    def paint(self, pts, color, dx=0.006, dy=0.005, seed=1):
        """Flat colour laid down slightly off the line, the way a brush misses."""
        p = soften(pts, True, 0.004, seed)
        self.sd.polygon([((x+0.016)*W, (y+0.020)*W) for x, y in p], fill=self.shadow)
        self.wd.polygon([((x+dx)*W, (y+dy)*W) for x, y in p], fill=color)

    def stroke(self, pts, closed, seed=0, amp=0.0035, w=STROKE):
        p = soften(pts, closed, amp, seed)
        px = [(x*W, y*W) for x, y in p]
        if closed:
            px.append(px[0])
        n = len(px); base = w*W
        for i in range(n-1):
            t = i/(n-1)
            lw = base*(0.90 + 0.10*math.sin(2*math.pi*2*t + seed))
            if not closed:
                lw *= max(0.42, math.sin(math.pi*t)**0.22)      # brush lifts at the ends
            r = lw/2.0
            self.idr.line([px[i], px[i+1]], fill=INK, width=max(1, int(lw)))
            self.idr.ellipse([px[i][0]-r, px[i][1]-r, px[i][0]+r, px[i][1]+r], fill=INK)

    def dot(self, cx, cy, r):
        self.idr.ellipse([(cx-r)*W, (cy-r)*W, (cx+r)*W, (cy+r)*W], fill=INK)

    def flatten(self):
        self.img.alpha_composite(self.shade.filter(ImageFilter.GaussianBlur(7.0*SS)))
        self.img.alpha_composite(self.wash.filter(ImageFilter.GaussianBlur(2.2*SS)))
        self.img.alpha_composite(self.ink.filter(ImageFilter.GaussianBlur(0.35*SS)))
        return self.img

# ---------------- grounds: painted, not flat ----------------
def ground(top, bottom, glow):
    g = Image.new("RGBA", (1, 256))
    for y in range(256):
        t = y/255.0
        g.putpixel((0, y), tuple(int(top[c]+(bottom[c]-top[c])*t) for c in range(3)) + (255,))
    img = g.resize((W, W), Image.BICUBIC)
    lit = Image.new("L", (W, W), 0)
    ImageDraw.Draw(lit).ellipse([-0.14*W, -0.32*W, 0.78*W, 0.62*W], fill=255)
    img.paste(Image.new("RGBA", (W, W), glow + (255,)),
              (0, 0), lit.filter(ImageFilter.GaussianBlur(0.24*W)).point(lambda v: int(v*0.62)))
    return img

def paper(img, strength=0.30):
    """Tooth. Two scales of grain, laid over everything so line and ground share one surface."""
    n = img.size[0]
    base = img.convert("RGB")
    fine   = Image.effect_noise((n//2, n//2), 26).resize((n, n), Image.BICUBIC)
    coarse = Image.effect_noise((n//14, n//14), 20).resize((n, n), Image.BICUBIC) \
                  .filter(ImageFilter.GaussianBlur(1.2))
    grain  = Image.blend(fine, coarse, 0.45)
    tex    = ImageChops.overlay(base, Image.merge("RGB", (grain,)*3))
    return Image.blend(base, tex, strength).convert("RGBA")

