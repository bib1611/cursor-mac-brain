#!/usr/bin/env bash
# Batch-transcribe the masterclass recordings in priority order.
# Resumable: skips any file whose .txt transcript already exists.
set -uo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
BRAIN="$(cd "$HERE/.." && pwd)"
QUEUE="$HERE/queue.txt"
OUT="$BRAIN/transcripts"
LOG="$HERE/transcribe.log"
MODEL="${WHISPER_MODEL:-base.en}"

mkdir -p "$OUT"
total=$(grep -c . "$QUEUE")
echo "=== transcription run started $(date) model=$MODEL total=$total ===" >> "$LOG"

i=0
while IFS= read -r f; do
  [ -z "$f" ] && continue
  i=$((i+1))
  base="$(basename "$f")"
  stem="${base%.*}"
  if [ -s "$OUT/$stem.txt" ]; then
    echo "[$i/$total] SKIP (exists): $stem" >> "$LOG"
    continue
  fi
  if [ ! -f "$f" ]; then
    echo "[$i/$total] MISSING: $f" >> "$LOG"
    continue
  fi
  echo "[$i/$total] START $(date '+%Y-%m-%d %H:%M:%S'): $base" >> "$LOG"
  if whisper "$f" --model "$MODEL" --language en --task transcribe \
       --output_dir "$OUT" --output_format txt --fp16 False --verbose False \
       >> "$LOG" 2>&1; then
    echo "[$i/$total] DONE  $(date '+%H:%M:%S'): $stem" >> "$LOG"
  else
    echo "[$i/$total] FAIL  $(date '+%H:%M:%S'): $base" >> "$LOG"
  fi
done < "$QUEUE"

echo "=== transcription run finished $(date) ===" >> "$LOG"
