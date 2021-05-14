class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        subdomains = dict()
        return_list = []

        for domain in cpdomains:
            count, domain = domain.split(" ")
            count_val = int(count)
            dom_parts = domain.split(".")
            for i in range(len(dom_parts)):
                key = ".".join(dom_parts[i:])
                if key not in subdomains:
                    subdomains[key] = count_val
                else:
                    subdomains[".".join(dom_parts[i:])] += count_val
        for key, val in subdomains.items():
            return_list.append("{} {}".format(val, key))
        return return_list