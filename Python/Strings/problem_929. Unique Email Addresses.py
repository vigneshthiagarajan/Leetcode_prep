class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        set_emails = set()
        for email in emails:
            localname = email.split("@")[0]
            domainname = email.split("@")[1]

            localname = localname.split("+")[0]
            localname = localname.replace(".", "")

            name = localname + "@" + domainname
            set_emails.add(name)
        return len(list(set_emails))
