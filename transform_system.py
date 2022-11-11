import re

def multiple_replace(string, rep_dict):
    pattern = re.compile("|".join([re.escape(k) for k in sorted(rep_dict,key=len,reverse=True)]), flags=re.DOTALL)
    return pattern.sub(lambda x: rep_dict[x.group(0)], string)



def transform_system(eq_system, dim):

    out_system = []

    for eq in eq_system:
        first = eq.split()[0]
        rest = " ".join(eq.split()[1:])
        #print(first)
        #print(rest)

        if dim == 2:
            rest = multiple_replace(rest, {
                '+':'-', 
                '-':'+',
                "x[7,7]": "a", 
                "x[8,8]": "b", 
            })
        elif dim == 3:
            rest = multiple_replace(rest, {
                '+':'-', 
                '-':'+',
                "x[26,24]": "a", 
                "x[26,26]": "b", 
                "x[27,27]": "c",
            })

        rest = rest.strip().strip("+").strip()
        #print(rest)
        result = "{} = \"{}\"".format(first, rest)
        result = result.replace("*", "")
        #result = result.replace("[", "_{").replace("]", "}")
        print(result)
        out_system.append(result)
        #out_system.append("$" + result + "$,\\")

    return out_system


if __name__ == "__main__":

    eq_system = ["x[6,6] - x[26,26] - x[27,27]"]
    #print("in:", eq_system)
    transform_system(eq_system)