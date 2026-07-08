import re

from app.models.timing import Timing, BPMChange


class TimingParser:

    def _get_tag(self, text: str, tag: str):

        pattern = rf"#{tag}:(.*?);"

        match = re.search(pattern, text, re.DOTALL)

        if match:
            return match.group(1).strip()

        return ""

    def parse(self, text: str) -> Timing:

        bpm_text = self._get_tag(text, "BPMS")

        bpms = []

        if bpm_text:

            for item in bpm_text.split(","):

                beat, bpm = item.split("=")

                bpms.append(
                    BPMChange(
                        beat=float(beat),
                        bpm=float(bpm)
                    )
                )

        return Timing(
            bpms=bpms,
            stops=[]
        )