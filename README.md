# Muse 2 BCI

A brain-computer interface built with a Muse 2 EEG headband (4 channels: TP9, AF7, AF8, TP10), streamed over Bluetooth with [muselsl](https://github.com/alexandrebarachant/muse-lsl).

## What's here
- `1_prepare_data.py` - splits recordings into epochs and extracts log band-power features (delta, theta, alpha, beta, gamma)
- `2_train_classifier.py` - trains an MLP classifier (scikit-learn) and reports accuracy
- `3_play_game.py` - real-time blink detection that sends a spacebar keypress to a browser game
- `psd/psd_analysis.py` - power spectral density (Welch) of recorded EEG
- `lessons/` - Python fundamentals practice that led up to this project

## Data
Raw recordings (`*.csv`) and trained models (`*.pkl`) are not included, since they are personal brain data. To reproduce, record your own with `python3 -m muselsl record`.

## Run
```
python3 -m muselsl stream --name <your Muse>
python3 3_play_game.py
```

## Results
- **4-class arm movements** (right arm, left arm, both arms, blink): 75% cross-validated accuracy on only 12 epochs (3 per class), so it is a proof of concept.
- **2-class blink vs. no-blink**: 100% cross-validated accuracy on 40 one-second epochs (15 no-blink, 25 blink). With a sample this small, that figure is probably optimistic.

## What I learned
- Band-power features need about 1 second of data, which was too slow for real-time gameplay. A blink is a brief, high-amplitude event.
- I switched to an adaptive threshold on the AF7/AF8 channels (rolling median baseline, minimum blink duration, cooldown), which responds sample by sample.
- Sensor contact matters most. Resting signal was ~400 µV with poor contact and ~50 µV after repositioning the headband.
- Next steps: longer recordings per class, a held-out test session, and replicating a published motor-imagery BCI.
