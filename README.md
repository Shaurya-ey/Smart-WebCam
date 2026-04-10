<h1 align="center">Smart WebCam</h1> 
Custom Raspberry Pi webcam with mic input, made for my desk setup. Built this instead of buying one to understand how everything works under the hood.
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
Basically, it’s a homemade webcam system. The Raspberry Pi takes input from the camera and microphone and sends it to the computer, so it behaves like a normal webcam. Instead of plug-and-play hardware, this is more like a small computer doing the same job.

## Why I Made This Project
I wanted a webcam for my desk, but instead of buying one I thought why not just build it. It started simple but then I kept adding things and learning more in the process. Setting up things like mic input, Wi-Fi and getting everything to work together took some time, but that’s what made it interesting.

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
| TRRS to TRS splitter | for mic | 2 | 2.15 |  |
| Mic | for audio input | 1 | 2.21 |  |
| Sound card | For audio output | 1 | 1.14 |  |
| OTG Cable | connecting sound card and raspi usb port | 1 | 0.90 |  |
| 5V 3A Power Supply | For powering raspi | 1 | 2.53 |  |
| CAD Models | Casings + Stands | 1 | 2.00 |  |
| 0.5W 28mm 8Ω Trumpet Speaker | Speaker | 1 | 0.30 |  |
| PAM8403 | Audio Amplifier | 1 | 0.66 |  |
| Heatsink | Heatsink for raspberry pi zero | 1 | 0.19 |  |
| INMP441 MEMS Microphone Module | Microphone | 1 | 1.99 |  |
| 64GB MicroSD Card | Memory disk for Raspi (MCU) | 1 | 15.16 |  |
| Raspberry Pi Zero | MCU | 1 | 18.80 |  |
| Raspberry Pi Camera Module 3 | Camera | 1 | 32.31 |  |
| Spring | 1 | 0.17 |  |
###  Total Cost: **$82.34**
