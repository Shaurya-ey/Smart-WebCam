<h1 align="center">Smart WebCam</h1> 
Custom Raspberry Pi webcam with mic input, made for my desk setup. Built this instead of buying one to understand how everything works.
<p align="center">
<img width="690" height="570" alt="Full with stand" src="https://github.com/user-attachments/assets/06e3ed7b-f4b7-403c-a329-607f621b21e4" />
</p>

 ---

 # 1. Overview
 This is a custom DIY webcam system built using a Raspberry Pi for my desk setup. Instead of buying a normal webcam, I wanted to make something on my own that I could actually understand and modify later. It’s a pretty simple setup but does the job and also helped me learn a lot about hardware + software working together.
 
 ## Features
- Raspberry Pi – Main brain of the system handling camera and mic input
- Camera Module – Captures video and sends it to the PC
- I2S Microphone – For voice input during calls or recording
- Wi-Fi Support – Lets the Pi connect to network for communication
- Compact Setup – Designed to sit on desk without taking much space
  
## What it is 
Basically, it’s a homemade webcam system. The Raspberry Pi takes input from the camera and microphone and sends it to the computer, so it behaves like a normal webcam. Instead of plug-and-play hardware, this is more like a small computer.

## Why I Made This Project
I wanted a webcam for my desk, but instead of buying one I thought why not just build it. It started simple but then I kept adding things and learning more in the process. Setting up things like mic input, Wi-Fi and getting everything to work together took some time.

## How To Use
- **Power:** on the Raspberry Pi and make sure it’s connected to Wi-Fi.
- **Run:** the main program on the Pi (this has to stay running).
- **Connect:** it to your PC and select it as camera and microphone in your meeting app.

---

# 2. Layouts
## Schematics
<img width="982" height="645" alt="Schematics" src="https://github.com/user-attachments/assets/03a56006-9094-41dc-998d-ab71dd2e6b73" />



## Case And Assembly
#### 1) Inner Casing Assembly
<p align="center">
<img width="400" height="300" alt="Inner case asse  2" src="https://github.com/user-attachments/assets/8246c20d-1996-46be-86e4-06468056e0ce" />
<img width="400" height="560" alt="Inner case asse  1" src="https://github.com/user-attachments/assets/30aea4fc-56c7-40a7-8cbc-c418ea244db7" />
</p>

#### 2) Outer Casing Assembly
<p align="center">
<img width="400" height="300" alt="Full case asse  2" src="https://github.com/user-attachments/assets/c74aa964-8b12-4fca-b884-99f410efaaee" />
<img width="400" height="506" alt="Full case asse" src="https://github.com/user-attachments/assets/7f692820-55c8-453b-af2d-18bbbb153295" />
</p>

#### 3) Stands
<p align="center">
<img width="450" height="350" alt="stand 1" src="https://github.com/user-attachments/assets/267dcec5-0238-4716-8804-b60023fc024b" />
<img width="400" height="350" alt="stand 2" src="https://github.com/user-attachments/assets/8a0c87cb-2e76-4343-83c7-c7ab2e56a590" />
<img width="592" height="420" alt="stand 1 5" src="https://github.com/user-attachments/assets/7e92645a-3cc2-4c84-84b7-6772aa0de636" />
</p>

#### 4) Overall assembly
<p align="center">
<img width="690" height="570" alt="Full with stand" src="https://github.com/user-attachments/assets/5c869896-e429-42b9-8200-be4686e961a6" />
</p>

# 3. BOM (Bill Of Materials)
## Bill of Materials (BOM)

| Item | Description | Quantity | Total Price (USD) | URL |
|------|------------|----------|------------------|-----|
| TRRS to TRS splitter | for mic | 2 | 2.15 | https://www.amazon.in/gp/product/B08GCZQT7D/ref=ox_sc_act_title_1?smid=A1WYWER0W24N8S&th=1 |
| Mic | for audio input | 1 | 2.21 | https://www.amazon.in/GWINGS-Microphone-Interviews-Compatibility-Smartphones/dp/B0GD2J1PQR/ref=sxin_14_pa_sp_search_thematic_sspa?content-id=amzn1.sym.7e2c8ac4-9f12-4bcd-9497-a8ae54bc8764%3Aamzn1.sym.7e2c8ac4-9f12-4bcd-9497-a8ae54bc8764&crid=1N2CLQORCCUTE&cv_ct_cx=wire%2Bmic&keywords=wire%2Bmic&pd_rd_i=B0GD2J1PQR&pd_rd_r=f3f9a633-aa48-4a49-b863-7474a3711b82&pd_rd_w=jLIB3&pd_rd_wg=RTxYd&pf_rd_p=7e2c8ac4-9f12-4bcd-9497-a8ae54bc8764&pf_rd_r=VK27QJMY2WY1NZKY25GW&qid=1775796535&sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D&sprefix=wiremic%2Caps%2C523&sr=1-5-66673dcf-083f-43ba-b782-d4a436cc5cfb-spons&aref=AD4x5wIcdW&sp_csd=d2lkZ2V0TmFtZT1zcF9zZWFyY2hfdGhlbWF0aWM&th=1 |
| Sound card | For audio output | 1 | 1.14 | https://robu.in/product/5-1-channel-usb-sound-card-for-raspberry-pi-and-computers/?gad_source=1&gad_campaignid=17416544847&gbraid=0AAAAADvLFWcaLEZ4BZxpNYTkApkTJ5lyC&gclid=CjwKCAjwnN3OBhA8EiwAfpTYehFyYkU7k9K_lXiWQS9rTXVuvbpnqzWhANsM9SaFnsCLTzoudtmhfhoCQh8QAvD_BwE#  |
| OTG Cable | connecting sound card and raspi usb port | 1 | 0.90 | https://robu.in/product/raspberry-pi-official-micro-usb-b-male-to-usb-a-female-adapter/?gad_source=1&gad_campaignid=19974686076&gbraid=0AAAAADvLFWclaudwu_pQwdub36csqIhwJ&gclid=CjwKCAjwnN3OBhA8EiwAfpTYehPJNi8-d6U0nbLRpdmAPpEEAtipRpUZ3efJJcSvzETvX5xz-H3hqRoCWzoQAvD_BwE |
| 5V 3A Power Supply | For powering raspi | 1 | 2.53 | https://robu.in/product/orange-5v-3a-power-supply-adapter-charger-with-micro-usb-plug/ |
| CAD Models | Casings + Stands | 1 | 2.00 | printing legion |
| 0.5W 28mm 8Ω Trumpet Speaker | Speaker | 1 | 0.30 | https://robu.in/product/0-5w-8ohm-trumpet-speaker-diameter-28mm/?gad_source=1&gad_campaignid=17427802703&gbraid=0AAAAADvLFWdwdvSUFSJIl7gt4S3iz58C-&gclid=Cj0KCQjwsdnNBhC4ARIsAA_3hejN1-d4zu4dOttRHCKA_VgE4x6-21bOFee4rh_wh22uVPcHH1gvgD8aAm9qEALw_wcB |
| PAM8403 | Audio Amplifier | 1 | 0.66 | https://robu.in/product/smartelex-pam8403-stereo-mini-class-d-audio-amplifier/?gad_source=1&gad_campaignid=18585959909&gbraid=0AAAAADvLFWf9poBXKnJ1WvIqZjHOJnVNZ&gclid=Cj0KCQjwsdnNBhC4ARIsAA_3heiZ63SWzzW7lcTJvHsz-yPUT-VRUdOtDFIUNyQFpS9vECSsSzwICY0aAmqrEALw_wcB |
| Heatsink | Heatsink for raspberry pi zero | 1 | 0.19 | https://robu.in/product/aluminum-heatsink-for-raspberry-pi/?gad_source=1&gad_campaignid=21296336107&gbraid=0AAAAADvLFWcZqI0XjFPMAZcna_aHTQget&gclid=CjwKCAjwpcTNBhA5EiwAdO1S9t07keo2cKPsQ2sHNPlL4Kzc7aBJWtGBFfTRRnoh8wZtnKaVIFmkLBoCJk4QAvD_BwE |
| INMP441 MEMS Microphone Module | Microphone | 1 | 1.99 | https://robu.in/product/inmp441-mems-high-precision-omnidirectional-microphone-module-i2s/ |
| 16GB MicroSD Card | Memory disk for Raspi (MCU) | 1 | 6.36| https://www.amazon.in/gp/product/B0GVJZ56K5/ref=ewc_pr_img_1?smid=AJ6SIZC8YQDZX&psc=1 |
| Raspberry Pi Zero | MCU | 1 | 22.45 | https://robu.in/product/raspberry-pi-zero-2-w-with-header |
| Raspberry Pi Camera Module 1.3 | Camera | 1 | 3.62 | https://robu.in/product/5mp-raspberry-pi-camera-module-w-hbv-ffc-cable?gclid=CjwKCAjwqazPBhALEiwAOuXqdIzl4dLuipezvb4f_adhpGrR0ODHmKrqNEJk8t6RmZvgmvLRcBY31hoCcpEQAvD_BwE&gbraid=0AAAAADvLFWfTuMASwQi7cJGyTOFSVa2hs&gad_source=1&gad_campaignid=17413441824 |
| Spring | 1 | for stand | 0.17  | https://robu.in/product/diy-kossel-delta-rostock-push-rod-spring-pack-of-2/ |
| wires and misc | 1 | 2.5 | |
###  Total Cost: **$50**
