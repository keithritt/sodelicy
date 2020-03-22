class Util:

  @staticmethod
  def isInt(text):
    try:
        int(text)
        return True
    except ValueError:
        return False
