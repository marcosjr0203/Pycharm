from prettytable import PrettyTable

startrek = PrettyTable()
startrek.field_names = ["Character name", "Actor name", "Function on Enterprise"]
startrek.add_rows(
    [
        ["James Kirk", "William Shatner", "Capitain"],
        ["Spock", "Leonard Nimoy", "First in Command"],
        ["Dr. McCoy", "DeForest Kelley", "Ship Doctor"],
        ["Uhura", "Nichele Nichols", "Communicator"],
        ["Sulu", "George Takei", "Helm"]
    ]
)
print(startrek)
