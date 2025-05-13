# CSCI 6704 — Advanced Topics in Computer Networks  
Dalhousie University · Fall 2024  
Author · Md Samshad Rahman (`@samshad`)

> Coursework portfolio for **CSCI 6704 – Advanced Topics in Computer Networks**.  
> Three assignments progress from signal‑level line‑coding to robust error detection, entirely in Python.

---

## 🌐  What you’ll find here

| Folder | Theme | Key tech & skills |
|--------|-------|-------------------|
| **A1** | *Networking theory & design questions* | Analytical write‑ups (PDF/DOCX) on throughput, latency, link utilisation, queuing, protocol design |
| **A2** | *Line‑coding & framing lab* | Python 3.11 · NumPy · Matplotlib<br>  • `exercise1.py` plots Unipolar, NRZ & Manchester waveforms<br>  • `exercise2.py` implements bit‑stuffing / de‑stuffing |
| **A3** | *CRC error‑detection lab* | Python CLI app & library<br>  • Generic CRC compute/verify functions<br>  • Burst‑error simulator (`error_detection_crc.py`)<br>  • Results logged to CSV + markdown analysis |

> ⭐ **Languages:** 100 % Python (plus PDF reports)  
> 📁 **Repo size:** 2 commits, 3 main directories

---

## 🧠  Learning outcomes

* **Physical‑layer signalling** – Visualised trade‑offs between Unipolar, NRZ and Manchester encoding.  
* **Frame delimitation & transparency** – Implemented HDLC‑style bit‑stuffing algorithms and verified correctness.  
* **Error‑detection maths** – Wrote generic CRC routines, then quantified detection probability against random burst errors.  
* **Python for network simulation** – Leveraged NumPy vectorisation and Matplotlib plotting—no heavyweight NS3/OMNeT++.  
* **Scientific reproducibility** – Each lab ships CLI flags, README, and sample CSV logs for easy reruns.

---

## 🛠  Toolchain

| Purpose | Stack |
|---------|-------|
| **Computation** | Python 3.11 · NumPy |
| **Visualisation** | Matplotlib |
| **Data logging** | Pandas · CSV |
| **Docs** | Markdown · PDF |

---

## 📂  Repository layout

```
.
├── A1/                    # Assignment 1 – theory/design report
├── A2/                    # Assignment 2 – line‑coding & bit‑stuffing labs
├── A3/                    # Assignment 3 – CRC error‑detection experiments
├── requirements.txt
└── LICENSE
```

Each assignment folder contains its own README (or inline docstrings) and sample output.

---

## 📄 Licence

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.  
© 2025 Md Samshad Rahman


