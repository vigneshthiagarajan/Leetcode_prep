class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:

        new_names = []
        present_names = dict()
        for name in names:
            if name not in present_names:
                present_names[name] = 1
                new_names.append(name)
            else:
                mod_name = name + "(" + str(present_names[name]) + ")"
                while mod_name in present_names:
                    present_names[name] += 1
                    mod_name = name + "(" + str(present_names[name]) + ")"
                present_names[mod_name] = 1
                new_names.append(mod_name)

        return new_names
