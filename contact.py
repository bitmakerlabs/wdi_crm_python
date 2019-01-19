class Contact:

  def __init__(self):
    """This method should initialize the contact's attributes"""


  @classmethod
  def create(cls):
    """This method should call the initializer,
    store the newly created contact, and then return it
    """

  @classmethod
  def all(cls):
    """This method should return all of the existing contacts"""

  @classmethod
  def find(cls):
    """ This method should accept an id as an argument
    and return the contact who has that id
    """

  def update(self):
    """ This method should allow you to specify
    1. which of the contact's attributes you want to update
    2. the new value for that attribute
    and then make the appropriate change to the contact
    """


  @classmethod
  def find_by(cls):
    """This method should work similarly to the find method above
    but it should allow you to search for a contact using attributes other than id
    by specifying both the name of the attribute and the value
    eg. searching for 'first_name', 'Betty' should return the first contact named Betty
    """


  @classmethod
  def delete_all(cls):
    """This method should delete all of the contacts"""


  def full_name(self):
    """Returns the full (first and last) name of the contact"""


  def delete(self):
    """This method should delete the contact
    HINT: Check the Array class docs for built-in methods that might be useful here
    """

  # Feel free to add other methods here, if you need them.

