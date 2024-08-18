class Animal: #class always on top
  
  def what_sound_does_it_make(self,flag):
    if flag.lower()=='bark':
      print("it's a dog")
    else:
      print("it's a human")
      
species_1= Animal()
species_1.what_sound_does_it_make('Bark')