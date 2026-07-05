count = 0


def bump():
    global count
    count += 1
    return count


type Bumped = bump()

created_lazily = count == 0
bumped_value = Bumped.__value__
bumped_again = Bumped.__value__

original_bumped = Bumped
type Bumped = bump()
rebinding_is_distinct = original_bumped is not Bumped and original_bumped != Bumped
rebinding_stays_lazy = count == 1
new_bumped_value = Bumped.__value__

type Waiting = later
later = 41

type SumAlias = later + 1

result = (
    Bumped.__name__ == "Bumped"
    and Bumped.__module__ == "__main__"
    and Bumped.__type_params__ == ()
    and Bumped.__parameters__ == ()
    and bool(Bumped)
    and not callable(Bumped)
    and Bumped is Bumped
    and Bumped == Bumped
    and created_lazily
    and bumped_value == 1
    and bumped_again == 1
    and rebinding_is_distinct
    and rebinding_stays_lazy
    and new_bumped_value == 2
    and count == 2
    and Waiting.__value__ == 41
    and getattr(SumAlias, "__value__") == 42
    and hasattr(SumAlias, "__value__")
    and getattr(SumAlias, "__name__") == "SumAlias"
    and not hasattr(SumAlias, "missing")
)

result
