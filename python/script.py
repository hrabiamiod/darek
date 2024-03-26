def create_html(links_file, output_html):
    with open(links_file, 'r') as file:
        links = file.read().splitlines()

    with open(output_html, 'w') as html_file:
        html_file.write('''<!DOCTYPE html>
<!-- Coding By CodingNepal - codingnepalweb.com -->
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8" />
    <title>Image Gallery with Lightbox | CodingLab</title>
    <link rel="stylesheet" href="style.css" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Fontawesome CDN Link -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
    />
  </head>
  <body>
    <section>
    <!--Okno lightboxa-->
      <div class="lightBox">
        <div class="lightBox_content">
          <i class="fas fa-times close"></i>
          <div class="logo_icons">
          </div>
          <div class="showImg">
            <div class="image">
              <img src="images/img1.jpg" alt="" />
            </div>
          </div>
        </div>
      </div>
    <!-- koniec okna lihghtboxa-->

    <!-- start galerii-->
    <div class="image-gallery">
        <div class="image-container">\n''')

        for link in links:
            html_file.write(f'''            <div class="image-box">
                <img class="gImg" src="{link}" alt="" />
            </div>\n''')

        html_file.write('''        </div>
    </div>
      </div>
    </section>
    <script>
      let body = document.querySelector("body"),
        lightBox = document.querySelector(".lightBox"),
        img = document.querySelectorAll(".gImg"),
        showImg = lightBox.querySelector(".showImg img"),
        close = lightBox.querySelector(".close");
      for (let image of img) {
        image.addEventListener("click", () => {
          showImg.src = image.src;
          lightBox.style.display = "block";
          body.style.overflow = "hidden";
          close.onclick = () => {
            lightBox.style.display = "none";
            body.style.overflow = "visible";
          };
        });
      }
    </script>
  </body>
</html>''')

# Example usage:
create_html('links.txt', 'output.html')

