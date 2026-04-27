# Overnight Image Optimization Summary

Stopped: 2026-04-26 01:35 Asia/Shanghai.

Scope:

- no commit
- no push
- no curated `assets/` writes
- generated outputs only under
  `tools/imagery/mote-comfy-client/assets/generated/light-mask-demo/overnight/`
- model cache repair only under the local Hugging Face cache

## Startup

- project_entry_file: `AGENTS.md`
- roadmap_lane: `tools` + `assets`
- implementation started: yes
- stop rule: stopped before 2026-04-26 10:00 Asia/Shanghai

## Hook Automatic Firing Loss

- loss_level: 2/10
- reason: `.agent/hook-events.jsonl` contains nearby `SessionStart` rows from
  the runtime, but this session did not capture a pre-start baseline row before
  opening the session.
- evidence: latest startup check found `SessionStart` rows around
  2026-04-26 01:10 Asia/Shanghai in `.agent/hook-events.jsonl`.
- repair: future hook verification should save `tail -n 1
  .agent/hook-events.jsonl` before launching the next session, then compare
  after startup.
- unknowns: none for this run.

## Segmentation-To-Lightmap Automation Loss

- loss_level: 5/10
- reason: large emitter segmentation is now repeatable and materially better,
  but tiny status lamps still fail and receiver `influence_map` generation is
  not solved by semantic segmentation.
- evidence: best large-emitter CLIPSeg results improved to terminal IoU 0.6999
  and window IoU 0.8626; best status lamp prompt sweep reached only IoU 0.0090
  and was rejected.
- repair: keep CLIPSeg + deterministic postprocess for large visible emitters;
  handle tiny emitters and receiver influence maps with explicit scene rules or
  a future Florence/GroundingDINO + SAM2 dependency plan.
- unknowns: whether a properly installed box-to-mask stack can localize the
  status lamps without hand-authored point hints.

## Best Result Paths

Best combined review surface:

- `assets/generated/light-mask-demo/overnight/best-clipseg-fine-postprocessed/`
- contact sheet:
  `assets/generated/light-mask-demo/overnight/best-clipseg-fine-postprocessed/mask-contact-sheet.png`
- metrics:
  `assets/generated/light-mask-demo/overnight/best-clipseg-fine-postprocessed/mask-comparison.md`

Best terminal mask:

- prompt: `computer terminal screen`
- threshold: 0.325
- postprocess: fill holes, then erode 3 times
- mask:
  `assets/generated/light-mask-demo/overnight/clipseg-fine-postprocess-sweep/terminal/thr-0.325/fill-then-erosion-3/masks/ai-terminal-screen-mask.png`
- IoU: 0.6999
- precision: 0.8671
- recall: 0.7840
- judgment: keep

Best window mask:

- prompt: `large circular window on the right`
- threshold: 0.600
- postprocess: fill holes, then erode 6 times
- mask:
  `assets/generated/light-mask-demo/overnight/clipseg-fine-postprocess-sweep/window/thr-0.600/fill-then-erosion-6/masks/ai-round-window-mask.png`
- IoU: 0.8626
- precision: 0.9098
- recall: 0.9433
- judgment: keep

Best status lamp attempt:

- prompt: `tiny glowing lamps`
- threshold: 0.35
- mask:
  `assets/generated/light-mask-demo/overnight/clipseg-status-prompt-sweep/tiny-glowing-lamps/thr-0.35/masks/ai-small-lights-mask.png`
- IoU: 0.0090
- precision: 0.0090
- recall: 0.9496
- judgment: reject

## Failed Attempts And Blockers

- `python` command failed because this shell has only `python3`; rerun with
  `python3` succeeded.
- CLIPSeg initially stalled because the local Hugging Face cache had an
  incomplete 0B `model.safetensors` blob.
- Repair command:

```bash
HF_HUB_DISABLE_XET=1 hf download CIDAS/clipseg-rd64-refined model.safetensors --cache-dir ~/.cache/huggingface/hub
```

- Florence/GroundingDINO/SAM2 were not attempted because local dependencies and
  model caches were missing.
- ComfyUI was reachable on the Windows GPU, but its node list did not include
  Florence, GroundingDINO, CLIPSeg, SAM, or SAM2 segmentation nodes.
- CLIPSeg prompt tuning did not repair status lamps.
- No attempt here solved receiver-surface `influence_map` generation.

## Morning Review: First Three Files

1. `tools/imagery/mote-comfy-client/assets/generated/light-mask-demo/overnight/SUMMARY.md`
2. `tools/imagery/mote-comfy-client/assets/generated/light-mask-demo/overnight/RUNLOG.md`
3. `tools/imagery/mote-comfy-client/assets/generated/light-mask-demo/overnight/best-clipseg-fine-postprocessed/mask-contact-sheet.png`
