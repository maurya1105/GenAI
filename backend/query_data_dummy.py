import time
#return ["Here's a comparison table outlining some key differences between Maven and Gradle, focusing on their project structure, conventions, and extensions:\n\n| Feature                 | Maven                                                                     | Gradle                                                                     |\n|-------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|\n| Project Structure      | Defines a `pom.xml` file at the root of the project, containing build information and dependencies.                | Defines a `build.gradle` file at the root of the project, with more flexible organization based on Gradle's plugin system.                       |\n| Conventions             | Employs strict naming and directory structure conventions (e.g., `src/main/java`, `src/promptTemplate/java`).                            | Employs less strict naming and directory structure conventions, allowing for greater flexibility in project organization.                          |\n| Dependency Management   | Uses a centralized repository (Maven Central) with dependency information stored in the `pom.xml` file.              | Allows for local and remote repositories, with dependencies defined in the `build.gradle` file or declared as project dependencies.                  |\n| Extensions             | Provides a set of built-in conventions (e.g., build phases, directory structures) and plugins. Plugins can extend functionality but are limited by Maven's fixed plugin architecture. | Offers an extensive ecosystem of community-created plugins that can be easily integrated into projects through the use of Gradle's powerful plugin system.            |\n| Build Speed             | Known for slower build times due to its XML configuration files and strict conventions.                              | Faster build times, as it uses a more efficient build script format (Groovy) and offers better caching and incremental builds.                       |\n| Multi-Project Support   | Supports multi-module projects through parent and child `pom.xml` files.                | Provides better multi-project support, allowing for easy management of multiple modules within the same build script or build configuration.         |\n| Flexibility             | Offers less flexibility due to its rigid structure and conventions.                   | Offers greater flexibility with more customizable project configurations based on the powerful plugin system.                                |\n\nIn summary, Maven and Gradle are both powerful build tools used in software development projects, but they have different strengths and limitations. While Maven is known for its rigid structure and centralized repository management, it offers a consistent and reliable approach to building Java projects. In contrast, Gradle provides greater flexibility, faster build times, and a more customizable approach to project configurations through the use of plugins. Both tools serve important purposes in software development, and the choice between them ultimately depends on the specific needs and preferences of your project.",["IDC","frfr"]]

promptTemplate=[]

#template 1
promptTemplate.append('''This is a test code block
```Python
print( "Hello World" )
for i in range( 50 ):
	print( "*" * i )
quit()
```
''')

#template 2
promptTemplate.append('''
Here is a test table
|Feature|Item 1|Item 2|
|-|-|-|
|Feature 1|Item 1 Quality 1|Item 2 Quality 1|
|Feature 2|Item 1 Quality 2|Item 2 Quality 2|
                      
''')
#template 3
promptTemplate.append('''
This is test **bold text**
This is a List
- ABCD
- EFGH
- IJKL
''')
def query_rag(queryText,history,promptIndex):
    time.sleep(2)
    #processing the query

    response=promptTemplate[promptIndex]
    #return format [response,sources]
    return [response,["Source 1","Source 2"]]

    
