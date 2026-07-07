---
title: "RRcard"
author: "rrop/rr-creator"
description: "A generic NFC business/hacker card"
created_at: "2026-07-07"
---

# 7th July: Entire PCB speedrun

Finished inserting and importing all components into KiCad, spent like 15 mins

<img width="1022" height="490" alt="image" src="https://github.com/user-attachments/assets/c3603c0e-3e93-4b1c-8f13-d61a6dcfc603" />

oook, so guys, im making this on kicad :)

and sooo, like the super smart person that I am, I spent 1 hour trying to figure out how to make a custom coil through python in kicad :)

and it didn't work

So I did some redditing and found there is a plugin that generates a coil to your exact specs

and now I wanna kill myself :)

😭 Now doing some math

```text
Fuck me, this took 2 hrs to figure out
=== Target inductance from chip capacitance ===
Chip: NT3H2111, C_chip = 50 pF
Target frequency: f = 13.56 MHz

L_target = 1 / ((2*pi*f)^2 * C_chip)

(2*pi*13.56e6) = 8.5208e7 rad/s
(8.5208e7)^2   = 7.2604e15
7.2604e15 * 50e-12 = 3.6302e5
L_target = 1 / 3.6302e5 = 2.7547e-6 H = 2.75 uH


=== Coil geometry ===
Formula: L = K1 * mu0 * n^2 * d_avg / (1 + K2*rho)
K1 = 2.25, K2 = 3.55  (circular spiral constants)
mu0 = 4*pi*1e-7 = 1.25664e-6 H/m

Chosen geometry:
  d_out        = 34 mm  = 0.034 m
  trace width  = 0.3 mm
  trace space  = 0.3 mm
  pitch        = width + space = 0.6 mm/turn
  turns/layer  = 3
  layers       = 2
  n (series)   = 3*2 = 6

Per-layer inner diameter:
  radial_buildup = turns_per_layer * pitch = 3 * 0.6mm = 1.8mm
  d_in = d_out - 2*radial_buildup = 34 - 2(1.8) = 30.4 mm = 0.0304 m

Average diameter and fill ratio:
  d_avg = (d_out + d_in)/2 = (34+30.4)/2 = 32.2 mm = 0.0322 m
  rho   = (d_out - d_in)/(d_out + d_in) = (34-30.4)/(34+30.4) = 3.6/64.4 = 0.05590

Denominator:
  1 + K2*rho = 1 + 3.55*0.05590 = 1 + 0.19845 = 1.19845

Numerator:
  K1 * mu0 * n^2 * d_avg
  = 2.25 * 1.25664e-6 * 36 * 0.0322
  = 2.8274e-6 * 36 = 1.01786e-4
  = 1.01786e-4 * 0.0322 = 3.2775e-6

L = 3.2775e-6 / 1.19845 = 2.7348e-6 H = 2.7348 uH

Result: 2.735 uH (calculated) vs 2.755 uH (target) -- 0.7% delta, within
formula's own uncertainty band.


=== Error propagation ===
Assume formula error range: +/-10-20%

L_low  = 2.75uH * 0.85 = 2.3375 uH
L_high = 2.75uH * 1.15 = 3.1625 uH

f_res = 1 / (2*pi*sqrt(L * C_chip))

At L_low  = 2.3375uH: f_res = 1/(2*pi*sqrt(2.3375e-6 * 50e-12))
  sqrt(2.3375e-6*50e-12) = sqrt(1.16875e-16) = 1.0811e-8
  f_res = 1/(2*pi*1.0811e-8) = 1/6.7925e-8 = 14.72 MHz

At L_high = 3.1625uH: f_res = 1/(2*pi*sqrt(3.1625e-6 * 50e-12))
  sqrt(3.1625e-6*50e-12) = sqrt(1.58125e-16) = 1.2575e-8
  f_res = 1/(2*pi*1.2575e-8) = 1/7.9013e-8 = 12.66 MHz

Result: actual resonance likely falls in 12.7-14.7 MHz range against a
13.56 MHz target.
```

Another 15 mins and schematic and footprint assignment done :)

<img width="1890" height="990" alt="image" src="https://github.com/user-attachments/assets/a28753c4-113f-42e1-92ac-f08fe85c264d" />

done routing in 15mins

<img width="606" height="392" alt="image" src="https://github.com/user-attachments/assets/cd7f21c9-c8f7-42d3-8144-6c845105538c" />

spent 45mins and finished front and back silkscreen

<img width="1265" height="781" alt="image" src="https://github.com/user-attachments/assets/2e91b74e-1b0a-49c4-8e9f-8423779f96d2" />

<img width="1353" height="785" alt="image" src="https://github.com/user-attachments/assets/250ccd08-5730-449b-8df0-f34f17b176c4" />

**Total time spent: 4.5 hours**
