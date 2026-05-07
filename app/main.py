def get_human_age(cat_age: int, dog_age: int) -> list:

    human_cat = 0
    human_dog = 0
    age_cat = cat_age
    age_dog = dog_age

    if not isinstance(cat_age, int):
        raise TypeError("Cat age must be an integer.")
    if not isinstance(dog_age, int):
        raise TypeError("Dog age must be an integer.")

    if age_cat >= 15:
        human_cat += 1
        age_cat -= 15
        if age_cat >= 9:
            human_cat += 1
            age_cat -= 9
            if age_cat >= 4:
                human_cat += age_cat // 4

    if age_dog >= 15:
        human_dog += 1
        age_dog -= 15
        if age_dog >= 9:
            human_dog += 1
            age_dog -= 9
            if age_dog >= 5:
                human_dog += age_dog // 5

    return [human_cat, human_dog]
