# AutoMapperAI — Estado y plan de acción

Este documento es el “checkpoint” del proyecto: qué está listo, qué sigue y en qué orden.

## Objetivo final

Audio (`.mp3`) → features (espectrograma/embeddings) → modelo IA → chart (4 flechas) → export `.sm` (compatible BeatX/StepMania).

## Alcance actual (importante)

- El dataset actual (`dataset/raw`) es **solo 4 flechas**: charts `dance-single`, filas de 4 caracteres.
- Aunque el formato `.sm` soporta `dance-double` (8 columnas), **por ahora lo ignoramos**.

## Estado actual (completado)

### Parser `.sm` (charts)

- ✅ `SMParser`: orquesta parseo de metadata, timing y charts.
- ✅ `ChartHeaderParser`: parsea las 5 líneas de cabecera del `#NOTES:`.
- ✅ `MeasureParser`: divide body en compases (separador `,`).
- ✅ `NoteParser`: convierte fila (`"0230"`) → `list[Note(lane, type)]`.
- ✅ Pipeline: cada `Measure` contiene:
  - `rows: list[str]`
  - `notes_by_row: list[list[Note]]`

### Tests

- ✅ `pytest` + tests mínimos del chart parser (sample + unit tests).

## Qué sigue (plan por fases)

### Fase A — Tiempo musical (necesario para alinear audio ↔ notas)

**Meta**: cada fila/nota debe saber su posición en beats y (luego) en segundos.

- ⬜ **Commit 7 — Beat position por fila**
  - Agregar a cada fila metadata como `measure_index`, `row_index`, `beat`.
  - Fórmula base: `beat = measure_index*4 + row_index*(4/rows_in_measure)`
  - Mini prueba en `backend/app/main.py` mostrando las primeras filas con su `beat`.

- ⬜ **Commit 8 — Beat → segundos (timeline)**
  - Usar `#BPMS` para convertir `beat` a `time_seconds`.
  - Mantenerlo simple: solo BPM changes (ya parseados).

- ⬜ **Commit 9 — Validación explícita (solo 4 flechas)**
  - Filtrar charts que no sean `dance-single`.
  - Rechazar filas de longitud != 4 (para dataset BeatX).

- ⬜ **Commit 10 — Tests de timing**
  - Tests unitarios de beat/seconds y de validación `dance-single`.

### Fase B — Dataset Builder

**Meta**: transformar `dataset/raw` → `dataset/processed` (JSON/NPZ) con ejemplos listos para ML.

- ⬜ Recorrer packs/canciones, parsear `.sm`
- ⬜ Guardar ejemplos (features/labels) + métricas (cuántas notas, cuántos charts, errores)

### Fase C — Audio + features

**Meta**: construir espectrogramas/embeddings y alinearlos con los targets (notas).

- ⬜ Loader `.mp3`
- ⬜ Mel-espectrograma
- ⬜ Ventanas de audio alineadas con timestamps de notas

### Fase D — ML baseline (v0)

**Meta**: primer modelo que predice grid 4-flechas.

- ⬜ Representación `time/beat × lane` + clases de nota
- ⬜ Train/val split
- ⬜ Métricas y primer “chart generado”

### Fase E — Export `.sm`

**Meta**: `Chart`/predicciones → texto `.sm`.

- ⬜ Writer `.sm`
- ⬜ Validar en StepMania/BeatX

