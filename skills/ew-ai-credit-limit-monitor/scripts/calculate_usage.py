#!/usr/bin/env python3
"""Calculate a weekly Codex allowance forecast from explicit account facts."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta


def parse_time(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("timestamps must include a UTC offset")
    return parsed


def calculate(remaining: float, cycle_start: datetime, reset_at: datetime, now: datetime) -> dict:
    if not 0 <= remaining <= 100:
        raise ValueError("remaining must be between 0 and 100")
    if not cycle_start < now < reset_at:
        raise ValueError("expected cycle_start < now < reset_at")

    used = 100.0 - remaining
    elapsed_hours = (now - cycle_start).total_seconds() / 3600
    hours_to_reset = (reset_at - now).total_seconds() / 3600
    burn_per_hour = used / elapsed_hours if used else 0.0
    burn_per_day = burn_per_hour * 24
    sustainable_per_day = remaining / hours_to_reset * 24

    projected_exhaustion = None
    gap_hours = None
    reduction_required_pct = 0.0
    if burn_per_hour > 0:
        projected_exhaustion = now + timedelta(hours=remaining / burn_per_hour)
        gap_hours = (reset_at - projected_exhaustion).total_seconds() / 3600
        if burn_per_day > sustainable_per_day:
            reduction_required_pct = (1 - sustainable_per_day / burn_per_day) * 100

    return {
        "remaining_pct": round(remaining, 2),
        "used_pct": round(used, 2),
        "elapsed_hours": round(elapsed_hours, 2),
        "hours_to_reset": round(hours_to_reset, 2),
        "burn_pct_per_day": round(burn_per_day, 2),
        "sustainable_pct_per_day": round(sustainable_per_day, 2),
        "reduction_required_pct": round(reduction_required_pct, 2),
        "projected_exhaustion": projected_exhaustion.isoformat() if projected_exhaustion else None,
        "gap_before_reset_hours": round(gap_hours, 2) if gap_hours is not None else None,
        "reset_at": reset_at.isoformat(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--remaining", type=float, required=True)
    parser.add_argument("--cycle-start", required=True)
    parser.add_argument("--reset-at", required=True)
    parser.add_argument("--now", required=True)
    args = parser.parse_args()
    result = calculate(
        args.remaining,
        parse_time(args.cycle_start),
        parse_time(args.reset_at),
        parse_time(args.now),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
