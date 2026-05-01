# Virtual Clinics

Concept sites for thirteen specialty virtual care programs.

Hosted via GitHub Pages at https://rdalvi.github.io/virtual-clinics/

## Structure

- `index.html` — landing page with all clinic cards
- `<slug>/index.html` — per-clinic concept page (13 of them)
- `assets/style.css` — shared stylesheet
- `build.py` — generates all HTML from clinic data + template
- `.nojekyll` — disables Jekyll processing on GitHub Pages

## Editing

All clinic content lives in the `CLINICS` list inside `build.py`. Edit there,
then regenerate:

```sh
python3 build.py
```

Commit the regenerated HTML alongside your `build.py` changes.

## Disclaimer

These pages describe hypothetical virtual clinics for design and discussion
purposes only. Nothing here is medical advice. No bookings are real. No
personal health information is collected.
