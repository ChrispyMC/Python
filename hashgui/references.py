class Resources:
  VERSION = "1.0.0"
  REVISION = "2020-06-23"
  """Options for hash functions."""
  HASH_OPTIONS = [
    #MD5
    "MD5",
    #SHA-3
    "SHA3-224",
    "SHA3-256",
    "SHA3-384",
    "SHA3-512",
    #SHA-2
    "SHA-224",
    "SHA-256",
    "SHA-384",
    "SHA-512",
    #SHA-1
    "SHA1",
    #SHAKE
    "SHAKE-128",
    "SHAKE-256",
    #BLAKE
    "BLAKE2B",
    "BLAKE2S"
  ]

class Window:
  #Geometry
  GEOMETRY = "1024x768"
  WIDTH = 1024
  HEIGHT = 768
  LABELTEXTSIZE = 10
  BUTTONTEXTSIZE = 12
  #Assets
  ICON = "icon.ico"
  BACKGROUND = "#2F2F2F"
  TEXT = "#FFFFFF"
  LABEL = "#303030"
  BUTTON = "#5F5F5F"
  BUTTONCTA = "#60A060"
  BUTTONLIGHT = "#F0F0F0"
  DROPDOWN = "#505050"
  #Light Colours
  #  "BACKGROUND": "#FFFFFF",
  #  "TEXT": "#000000",
  #  "LABEL": "#AFAFAF",
  #  "BUTTON": "#AFAFAF",
  #  "DROPDOWN": "#A0A0A0"
  #Dark Colours
  #  "BACKGROUND": "#2F2F2F",
  #  "TEXT": "#FFFFFF",
  #  "LABEL": "#303030",
  #  "BUTTON": "#5F5F5F",
  #  "DROPDOWN": "#505050"

class WindowMenu:
  #GEOMETRY
  GEOMETRY = "640x360"
  WIDTH = 640
  HEIGHT = 360