from sqlfluff.core.rules.base import BaseRule, LintResult
from sqlfluff.core.rules.crawlers import RootOnlyCrawler

class Rule_ABU_D001(BaseRule):
    """Require a header comment at the start of each SQL file.

    The first non-empty line must start with '--' or '/*'.
    """

    code = "ABU_D001"
    description = "Require a header comment at the start of each SQL file."
    groups = ("all",)

    # NEW (required): define how the rule is applied/traverses the file
    crawl_behaviour = RootOnlyCrawler()

    def _eval(self, context):
        raw = context.segment.raw or ""
        for line in raw.splitlines():
            if line.strip() == "":
                continue
            s = line.lstrip()
            if s.startswith("--") or s.startswith("/*"):
                return None
            # anchor at file root (usually shows line 1/col 1)
            return LintResult(anchor=context.segment)
        return LintResult(anchor=context.segment)
