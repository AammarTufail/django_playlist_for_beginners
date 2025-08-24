from django.http import HttpResponse
from django.shortcuts import render
from courses.models import Courses
# # home view
# def home(request):
#     return HttpResponse("Welcome to the home page by Codanics. for Home Page.")

def home(request):
    courses = Courses.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'index.html', context)

def blogs(request):
    return render(request, 'blogs.html')


# # blogs view
# def blogs(request):
#     html_content = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>Codanics Blogs</title>
#         <style>
#             body {
#                 font-family: Arial, sans-serif;
#                 max-width: 800px;
#                 margin: 0 auto;
#                 padding: 20px;
#                 background-color: #f5f5f5;
#             }
#             .container {
#                 background-color: white;
#                 padding: 30px;
#                 border-radius: 10px;
#                 box-shadow: 0 2px 10px rgba(0,0,0,0.1);
#             }
#             h1 {
#                 color: #333;
#                 text-align: center;
#                 margin-bottom: 30px;
#             }
#             .blog-post {
#                 border-left: 4px solid #007bff;
#                 padding-left: 20px;
#                 margin: 20px 0;
#             }
#         </style>
#     </head>
#     <body>
#         <div class="container">
#             <h1>Welcome to Codanics Blogs</h1>
#             <div class="blog-post">
#                 <h3>Latest Programming Tips</h3>
#                 <p>Discover the latest programming techniques and best practices.</p>
#             </div>
#             <div class="blog-post">
#                 <h3>Web Development Insights</h3>
#                 <p>Learn about modern web development frameworks and tools.</p>
#             </div>
#         </div>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_content)
