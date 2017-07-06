# Schedule-Local
Scheduling Program used in 2016


# Problems to be solved.

1. Version Control: “How do we track changes?” This affects both input and output.
1. Too many files
    * Import directly from google sheets
    * Central repository/database.
1. Automatic Section Control
    * Eliminate conflicts
    * Class number limit
1. Web-based compilation: Someway for anyone to execute program.
    1. Spits out any exceptions i.e. typos or classes that don’t exist. Ask user to continue or exit.
    1. Spits out changes from last run. Ask user to continue or exit.
    1. Executes schedule.
    * What should the user see at this point?
    * Must work with version control.
    * Must work with  new database.
1. Flow: Needs to be orderly. Not guesswork.
    * Too cumbersome: see (1-4)
    * Relies too much on one person.
    * System should eliminate myopic people: “Why can’t we just make this change.”
    * Decision making should be obvious.
    * Prevent playing favorites.
        * Trade-offs should be apparent.
    * What is it that Sylvia or I am doing? Can we teach a computer to do it?
1. Analysis
    * Where does the program stop? I.e. What is the final output: see 4.a)
    * What tools would be useful?
        1. Selection/Comparison: Can/Should this be automated
        1. Identify problems: see 4.e)
1. Output for parents
    * Automate a pretty version
    * Formal Names for classes
    * Proposed Solution
        1. Use the type column
        1. Types: Teacher/ Part-Time Teacher: Can put additional time constraints.
        1. Room: Has constraint but nor formal output
        1. Student: More Formal output. No time constraints.
        1. Classes: completely different object
1. Input: Survey as possible solution.
    * Will give us preferences in addition to telling us what courses we need to provide.
    * Eliminate back & Forth: see 5
    * Seperate likes/wants from needs.
    * Input will understand AND vs OR vs XOR.
        * This will be complicated to communicate. 
        * Also need to find the correct way to input and store this information.
