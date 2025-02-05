class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_store = {}
        for i in cpdomains:
            num_and_dom = i.split()
            num = int(num_and_dom[0])
            for index_of_char in range(len(num_and_dom[1])-1,-1,-1):
                if num_and_dom[1][index_of_char] == ".":
                    domain_store[num_and_dom[1][index_of_char+1:]] = domain_store.get(num_and_dom[1][index_of_char+1:],0) + num 

                elif index_of_char == 0:
                    domain_store[num_and_dom[1][index_of_char:]] = domain_store.get(num_and_dom[1][index_of_char:],0) + num 
                    break
        domain_with_count = [f"{count} {domain}" for domain,count in domain_store.items()]
        return domain_with_count
                
                    
        