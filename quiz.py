import streamlit as st
import random

# Define questions and answers for each module
questions = {
    "HTML": [
        {"question": "What is the main focus of the 'Intro to Semantic HTML' lesson?", "options": ["Understanding HTML structure", "Learning CSS styles", "JavaScript basics"], "answer": "Understanding HTML structure"},
        {"question": "Describe the key points discussed in the 'More on semantics' lesson.", "options": ["Importance of semantic elements", "Basic HTML tags", "CSS properties"], "answer": "Importance of semantic elements"},
        {"question": "What are the uses of semantics as explained in the 'Uses for semantics' lesson?", "options": ["Improving accessibility and SEO", "Enhancing JavaScript functionality", "Designing CSS layouts"], "answer": "Improving accessibility and SEO"},
        {"question": "How does the 'Intro to Semantic HTML' lesson contribute to understanding HTML structure?", "options": ["By explaining semantic tags", "By covering JavaScript syntax", "By demonstrating CSS techniques"], "answer": "By explaining semantic tags"},
        {"question": "What improvements could be suggested for the 'More on semantics' lesson?", "options": ["Include more examples", "Add JavaScript integration", "Focus on CSS"], "answer": "Include more examples"},
        {"question": "How does semantic HTML enhance accessibility?", "options": ["By providing meaningful tags", "By adding interactive elements", "By improving script performance"], "answer": "By providing meaningful tags"},
        {"question": "What are the best practices for using semantic elements?", "options": ["Use proper tags for content", "Avoid inline styles", "Include JavaScript functions"], "answer": "Use proper tags for content"},
        {"question": "Compare the 'Intro to Semantic HTML' lesson with other HTML lessons.", "options": ["Focus on semantics vs. syntax", "Basics vs. advanced topics", "Static vs. dynamic content"], "answer": "Focus on semantics vs. syntax"},
        {"question": "How does 'More on semantics' influence modern web development?", "options": ["Encourages best practices", "Promotes outdated techniques", "Focuses on legacy code"], "answer": "Encourages best practices"},
        {"question": "Explain the practical applications of semantic HTML in real-world projects.", "options": ["Improves SEO and accessibility", "Increases file size", "Reduces browser compatibility"], "answer": "Improves SEO and accessibility"},
        {"question": "What challenges might a developer face when implementing semantic HTML?", "options": ["Understanding tag usage", "Managing JavaScript interactions", "Optimizing CSS performance"], "answer": "Understanding tag usage"},
        {"question": "How do the lessons in this course align with industry standards?", "options": ["Follow best practices", "Use outdated methods", "Ignore current trends"], "answer": "Follow best practices"},
        {"question": "What is the significance of using semantic tags in HTML?", "options": ["Improves readability and SEO", "Reduces code complexity", "Eliminates the need for JavaScript"], "answer": "Improves readability and SEO"},
        {"question": "How can semantic HTML impact SEO?", "options": ["By providing meaningful content", "By adding more images", "By increasing script execution"], "answer": "By providing meaningful content"},
        {"question": "Discuss the role of semantic HTML in responsive design.", "options": ["Enhances content structure", "Increases loading time", "Requires additional scripts"], "answer": "Enhances content structure"},
        {"question": "What are the key differences between semantic and non-semantic HTML elements?", "options": ["Meaningful vs. generic tags", "Inline vs. block elements", "Static vs. dynamic content"], "answer": "Meaningful vs. generic tags"},
        {"question": "How does the 'Uses for semantics' lesson address common misconceptions?", "options": ["Clarifies tag purposes", "Promotes deprecated tags", "Focuses on obsolete techniques"], "answer": "Clarifies tag purposes"},
        {"question": "What are some advanced techniques for using semantic HTML?", "options": ["Combining tags effectively", "Avoiding semantic tags", "Using non-standard elements"], "answer": "Combining tags effectively"},
        {"question": "How can you verify that your HTML is semantically correct?", "options": ["Using validation tools", "Manually checking each tag", "Relying on browser rendering"], "answer": "Using validation tools"},
        {"question": "What are some tools or resources for learning more about semantic HTML?", "options": ["Online tutorials and validators", "JavaScript frameworks", "CSS libraries"], "answer": "Online tutorials and validators"},
    ],
    "CSS": [
        {"question": "What is covered in the 'Special Selectors' lesson of the CSS course?", "options": ["Advanced selector techniques", "Basic CSS properties", "JavaScript integration"], "answer": "Advanced selector techniques"},
        {"question": "Explain the concept of 'Sibling Selectors' as taught in the CSS course.", "options": ["Selectors targeting adjacent elements", "Selectors for classes", "Selectors for IDs"], "answer": "Selectors targeting adjacent elements"},
        {"question": "Describe the 'Adjacent Selectors' and their application according to the CSS course.", "options": ["Selectors for immediate siblings", "Selectors for nested elements", "Selectors for all elements"], "answer": "Selectors for immediate siblings"},
        {"question": "How does the 'Special Selectors' lesson enhance understanding of CSS?", "options": ["By introducing advanced selectors", "By focusing on basic styles", "By covering JavaScript functionality"], "answer": "By introducing advanced selectors"},
        {"question": "What is the significance of 'Sibling Selectors' in CSS?", "options": ["Targeting elements based on sibling relationships", "Styling elements by IDs", "Defining global styles"], "answer": "Targeting elements based on sibling relationships"},
        {"question": "How can 'Adjacent Selectors' be used in real-world CSS design?", "options": ["Styling list items following headings", "Styling all paragraphs", "Defining global font styles"], "answer": "Styling list items following headings"},
        {"question": "What are the key differences between 'Special Selectors' and other CSS selectors?", "options": ["Advanced vs. basic selectors", "Static vs. dynamic styles", "Inline vs. block styles"], "answer": "Advanced vs. basic selectors"},
        {"question": "How do 'Sibling Selectors' contribute to CSS layout and styling?", "options": ["By enabling targeted styling based on sibling relationships", "By defining overall page styles", "By integrating with JavaScript"], "answer": "By enabling targeted styling based on sibling relationships"},
        {"question": "What are some examples of effective use of 'Adjacent Selectors'?", "options": ["Styling list items following headings", "Styling all paragraphs", "Defining global font styles"], "answer": "Styling list items following headings"},
        {"question": "How can you test and debug CSS selectors in your projects?", "options": ["Using browser developer tools", "Manually reviewing CSS files", "Ignoring selector issues"], "answer": "Using browser developer tools"},
        {"question": "What are the challenges of using advanced CSS selectors?", "options": ["Complexity and browser compatibility", "Simplicity and ease of use", "Lack of functionality"], "answer": "Complexity and browser compatibility"},
        {"question": "How do the concepts of 'Special Selectors' apply to responsive design?", "options": ["Targeting specific elements for different screen sizes", "Applying global styles", "Ignoring screen sizes"], "answer": "Targeting specific elements for different screen sizes"},
        {"question": "What role do 'Sibling Selectors' play in managing CSS rules?", "options": ["Allowing targeted styling based on element relationships", "Applying styles universally", "Defining JavaScript interactions"], "answer": "Allowing targeted styling based on element relationships"},
        {"question": "How can 'Adjacent Selectors' be optimized for performance?", "options": ["Minimizing selector complexity", "Using more selectors", "Focusing only on layout styles"], "answer": "Minimizing selector complexity"},
        {"question": "What are some common mistakes with 'Special Selectors'?", "options": ["Overcomplicating selectors", "Ignoring best practices", "Using too few selectors"], "answer": "Overcomplicating selectors"},
        {"question": "How does the course content on CSS selectors compare to other resources?", "options": ["Provides comprehensive coverage", "Focuses only on basics", "Ignores advanced techniques"], "answer": "Provides comprehensive coverage"},
        {"question": "What are the best practices for using 'Sibling Selectors'?", "options": ["Use them judiciously for performance", "Overuse them for complex styles", "Avoid them in favor of class selectors"], "answer": "Use them judiciously for performance"},
        {"question": "How can you apply 'Adjacent Selectors' in a real-world project?", "options": ["Styling elements that are directly following other elements", "Applying styles to all elements", "Defining global layout rules"], "answer": "Styling elements that are directly following other elements"},
        {"question": "Discuss the impact of 'Special Selectors' on CSS maintainability.", "options": ["Can improve maintainability with clear rules", "Can make CSS harder to maintain", "Has no impact on maintainability"], "answer": "Can improve maintainability with clear rules"},
    ],
    "JavaScript": [
        {"question": "What are the key features of JavaScript covered in the course?", "options": ["Core language features and syntax", "Advanced server-side programming", "Basic HTML structures"], "answer": "Core language features and syntax"},
        {"question": "How does the course explain 'JavaScript Objects'?", "options": ["Defining and using objects", "Creating basic functions", "Understanding CSS properties"], "answer": "Defining and using objects"},
        {"question": "What is the purpose of 'Functions' in JavaScript as taught in the course?", "options": ["Encapsulating reusable code", "Defining HTML elements", "Applying CSS styles"], "answer": "Encapsulating reusable code"},
        {"question": "Describe the role of 'JavaScript Objects' in programming.", "options": ["Storing and manipulating data", "Defining HTML structure", "Applying global styles"], "answer": "Storing and manipulating data"},
        {"question": "How does the course approach teaching 'Functions' in JavaScript?", "options": ["By demonstrating practical examples", "By focusing on theoretical concepts", "By ignoring real-world applications"], "answer": "By demonstrating practical examples"},
        {"question": "What are some advanced topics in JavaScript covered in the course?", "options": ["Asynchronous programming", "Basic syntax", "HTML structure"], "answer": "Asynchronous programming"},
        {"question": "How does the course ensure a solid understanding of 'JavaScript Objects'?", "options": ["By providing hands-on exercises", "By focusing only on theory", "By ignoring practical examples"], "answer": "By providing hands-on exercises"},
        {"question": "What is the significance of mastering 'Functions' in JavaScript?", "options": ["Enables code reuse and modularity", "Focuses on styling web pages", "Defines static HTML content"], "answer": "Enables code reuse and modularity"},
        {"question": "What are the common challenges faced when learning 'JavaScript Objects'?", "options": ["Understanding object properties and methods", "Learning basic HTML", "Applying CSS styles"], "answer": "Understanding object properties and methods"},
        {"question": "How does the course address practical uses of 'Functions' in JavaScript?", "options": ["By incorporating real-world examples", "By focusing on theoretical aspects", "By ignoring practical scenarios"], "answer": "By incorporating real-world examples"},
        {"question": "How can you apply 'JavaScript Objects' in your projects?", "options": ["To manage complex data structures", "To style web pages", "To define static HTML content"], "answer": "To manage complex data structures"},
        {"question": "What are some best practices for using 'Functions' in JavaScript?", "options": ["Writing reusable and modular code", "Avoiding function definitions", "Using global variables"], "answer": "Writing reusable and modular code"},
        {"question": "How does the course content on JavaScript compare to industry standards?", "options": ["Aligns well with current practices", "Focuses on outdated techniques", "Ignores modern JavaScript features"], "answer": "Aligns well with current practices"},
        {"question": "What resources are recommended for further learning about JavaScript objects?", "options": ["Documentation and tutorials", "CSS frameworks", "HTML validators"], "answer": "Documentation and tutorials"},
        {"question": "How does mastering 'Functions' benefit a JavaScript developer?", "options": ["Improves code efficiency and maintainability", "Focuses only on styling", "Defines HTML structures"], "answer": "Improves code efficiency and maintainability"},
        {"question": "What are the practical applications of advanced JavaScript topics?", "options": ["Building dynamic web applications", "Creating static HTML pages", "Styling web pages"], "answer": "Building dynamic web applications"},
    ]
}

def generate_quiz(module):
    if module not in questions:
        st.error("Invalid module selected!")
        return
    
    module_questions = questions[module]
    random.shuffle(module_questions)
    quiz_questions = module_questions[:25]  # Limit to 25 questions
    return quiz_questions

def boost_performance(score):
    if score < 60:
        st.write("### Performance Improvement Recommendations")
        st.write("1. **Review Course Material**: Focus on the areas where you struggled the most.")
        st.write("2. **Practice Regularly**: Spend extra time practicing questions and concepts.")
        st.write("3. **Seek Help**: Don't hesitate to ask for help from peers or instructors.")
        st.write("4. **Utilize Resources**: Use online resources and tutorials to reinforce your learning.")
    else:
        st.write("### Congratulations!")
        st.write("You scored well! Keep up the good work.")

def provide_resources_and_videos(module):
    if module == "HTML":
        st.write("### Additional Resources for HTML")
        st.write("[MDN Web Docs: HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)")
        st.write("[W3Schools: HTML Tutorial](https://www.w3schools.com/html/)")
        st.write("[FreeCodeCamp: HTML and HTML5](https://www.freecodecamp.org/learn/responsive-web-design/#basic-html-and-html5)")
        st.write("### Self-Tutor Videos for HTML")
        st.video("https://www.youtube.com/watch?v=5bMdjkfvONE&t=517s")  # Example YouTube video URL
        st.video("https://www.youtube.com/watch?v=qz0aGYrrlhU")  # Another example YouTube video URL
    elif module == "CSS":
        st.write("### Additional Resources for CSS")
        st.write("[MDN Web Docs: CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)")
        st.write("[W3Schools: CSS Tutorial](https://www.w3schools.com/css/)")
        st.write("[FreeCodeCamp: CSS](https://www.freecodecamp.org/learn/responsive-web-design/#basic-css)")
        st.write("### Self-Tutor Videos for CSS")
        st.video("https://www.youtube.com/watch?v=U01kR2Qe_L4")  # Example YouTube video URL
        st.video("https://www.youtube.com/watch?v=nu_pCVPKzTk")  # Another example YouTube video URL
    elif module == "JavaScript":
        st.write("### Additional Resources for JavaScript")
        st.write("[MDN Web Docs: JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)")
        st.write("[W3Schools: JavaScript Tutorial](https://www.w3schools.com/js/)")
        st.write("[FreeCodeCamp: JavaScript Algorithms and Data Structures](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)")
        st.write("### Self-Tutor Videos for JavaScript")
        st.video("https://www.youtube.com/watch?v=PkZNo7MFNFg")  # Example YouTube video URL
        st.video("https://www.youtube.com/watch?v=uh4gG7LbDPQ")  # Another example YouTube video URL

def main():
    st.title("Quiz Generator")
    
    module = st.selectbox("Select a module", ["Choose a Module", "HTML", "CSS", "JavaScript"])
    questions = generate_quiz(module)
    
    if questions:
        with st.form("quiz_form"):
            score = 0
            total_questions = len(questions)
            
            for q in questions:
                st.write(q["question"])
                answer = st.radio("Choose your answer:", q["options"], key=q["question"])
                if answer == q["answer"]:
                    score += 1

            submit_button = st.form_submit_button("Submit")

            if submit_button:
                st.write(f"Your score: {score}/{total_questions}")
                boost_performance(score)
                provide_resources_and_videos(module)

if __name__ == "__main__":
    main()