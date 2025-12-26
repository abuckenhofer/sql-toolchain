from sqlfluff.core.plugin import hookimpl

@hookimpl
def get_rules():
    from sqlfluff_rules.rules import Rule_ABU_D001
    return [Rule_ABU_D001]
