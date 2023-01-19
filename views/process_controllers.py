import views.validated_input as vi
import configs.language as lang

def exit_process(next_process):
    """ this function is to get user confirmation to continue the process or exit.
    """
    next = int(vi.defined_values(
            lang.str_by_lang_key("input_10_climbed").format(next_process)
            ,(0,1)
            ,True
        ))
    return next == 0
        