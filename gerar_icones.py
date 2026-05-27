#!/usr/bin/env python3
"""Gera os ícones PNG do Canto Livre a partir de SVG."""
import subprocess, os, sys

svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <rect width="512" height="512" rx="100" fill="#1a3a2a"/>
  <circle cx="256" cy="256" r="160" fill="#2a5c3f"/>
  <!-- pássaro estilizado -->
  <ellipse cx="256" cy="270" rx="70" ry="50" fill="#6abf8a"/>
  <ellipse cx="256" cy="248" rx="40" ry="38" fill="#6abf8a"/>
  <!-- asa -->
  <ellipse cx="210" cy="265" rx="55" ry="22" fill="#3d8a5e" transform="rotate(-20,210,265)"/>
  <!-- bico -->
  <polygon points="296,240 320,250 296,258" fill="#e8a840"/>
  <!-- olho -->
  <circle cx="284" cy="244" r="6" fill="#0f2318"/>
  <circle cx="286" cy="242" r="2" fill="#c8ecd6"/>
  <!-- ondas sonoras -->
  <path d="M330 220 Q350 248 330 276" stroke="#6abf8a" stroke-width="8" fill="none" stroke-linecap="round" opacity="0.7"/>
  <path d="M348 208 Q378 248 348 288" stroke="#6abf8a" stroke-width="6" fill="none" stroke-linecap="round" opacity="0.4"/>
</svg>'''

os.makedirs('icons', exist_ok=True)

with open('icons/icon.svg', 'w') as f:
    f.write(svg)

for size in [192, 512]:
    result = subprocess.run(
        ['convert', '-background', 'none', '-resize', f'{size}x{size}',
         'icons/icon.svg', f'icons/icon-{size}.png'],
        capture_output=True
    )
    if result.returncode != 0:
        # fallback: criar PNG simples com Python sem ImageMagick
        print(f"ImageMagick não disponível, gerando ícone simples {size}x{size}...")
        try:
            from PIL import Image, ImageDraw
            img = Image.new('RGBA', (size, size), (0,0,0,0))
            draw = ImageDraw.Draw(img)
            draw.rounded_rectangle([0,0,size-1,size-1], radius=size//5, fill='#1a3a2a')
            cx, cy, r = size//2, size//2, size//3
            draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill='#2a5c3f')
            br = int(r*0.65)
            draw.ellipse([cx-br, cy-br+r//8, cx+br, cy+br+r//8], fill='#6abf8a')
            img.save(f'icons/icon-{size}.png')
            print(f"  ✓ icon-{size}.png gerado")
        except ImportError:
            # fallback mínimo: criar arquivo PNG válido
            import struct, zlib
            def make_png(size, bg=(26,58,42)):
                def chunk(name, data):
                    c = zlib.crc32(name+data) & 0xffffffff
                    return struct.pack('>I',len(data))+name+data+struct.pack('>I',c)
                sig = b'\x89PNG\r\n\x1a\n'
                ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0))
                raw = b''.join(b'\x00'+bytes(bg)*size for _ in range(size))
                idat = chunk(b'IDAT', zlib.compress(raw))
                iend = chunk(b'IEND', b'')
                with open(f'icons/icon-{size}.png','wb') as f:
                    f.write(sig+ihdr+idat+iend)
                print(f"  ✓ icon-{size}.png gerado (cor sólida)")
            make_png(size)
    else:
        print(f"  ✓ icon-{size}.png gerado")

print("\nÍcones prontos em icons/")
