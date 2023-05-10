class Software():

    def __init__(self, usage, language, versions):
        self.usage = usage
        self.language = language
        self.versions = versions
    
    def __str__(self):  #similar to Java's toString()
        return f"Software will be used for {self.usage}. It will be in {self.language} and it will have {self.versions} versions."
    
    def __del__(self):  #deletes object from the memory of the computer
        print("A version of the software has been removed.")
    
    def __len__(self):
        return self.versions    #we can return whatever we want to consider as length of an object of this class 

my_software = Software("Business Automation", "English", 4)
print(my_software)

# del(my_software)
# print(my_software)

print(len(my_software))
