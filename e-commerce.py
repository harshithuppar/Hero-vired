from  flask  import Flask , render_template

e_app = Flask(__name__)

@e_app.route('/')
def hello():
    return 'Hello!,Welcome to E-commerce App'

product = [
    {'name': 'iphone', 'price': '999', 'description': 'mobile', 'url': 'https://www.google.com/search?q=iphone+images+for+wallpaper&tbm=isch&ved=...'},
    {'name': 'Book', 'price': '799', 'description': 'Books', 'url': 'https://www.google.com/search?q=books&tbm=isch&ved=...'},
    {'name': 'TV', 'price': '6799', 'description': 'electronics', 'url': 'https://www.google.com/search?q=TV&sca_esv=595369570&tbm=isch&...'}
]

@e_app.route('/product')
def display_product():
  return render_template('product.html',product=product)


if __name__ == "__main__":
 e_app.run()