

class meta_generator():

    @classmethod
    def determine_meta_data(filename: str) -> list:
        test = "META_" + filename + "_ITWORKS"
        return [test, test, test]
