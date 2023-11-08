# Custom gallery screen and object, because I don't give enough of a shit to try to make the renpy default gallery work
# Probably made way too general, but I want to use this maybe for future projects, so...

init python:
    
    class CustomGalleryImage:
        def __init__(self, image, name: str = "", locked: bool = False):
            self.name = name
            self.image = image
            self.locked = locked

        def unlock(self):
            self.locked = False

    class CustomGalleryPage:

        def __init__(self):
            self.images = []
        
        def add_image(self, image: CustomGalleryImage):
            self.images.append(image)
        
        def unlock_name(self, name: str):
            for img in self.images:
                if img.name == name:
                    img.unlock()
    
    # This is the only one a screen should interface with once the gallery is set up
    class CustomGallery:
        def __init__(self):
            self.pages = []
            self.curr_page = 0

        def add_page(self, page: CustomGalleryPage):
            self.pages.append(page)

        def unlock_index(self, page_index, image_index):
            self.pages[page_index].images[image_index].unlock()

        def unlock_name(self, name: str):
            for page in self.pages:
                page.unlock_name(name)

        def change_page(self, page_num: int):
            self.curr_page = page_num
            if self.curr_page >= len(self.pages):
                self.curr_page = len(self.pages) - 1
            if self.curr_page <= -1:
                self.curr_page = 0

        def increment_page(self):
            self.curr_page += 1
            if self.curr_page >= len(self.pages):
                self.curr_page = 0
        
        def decrement_page(self):
            self.curr_page -= 1
            if self.curr_page <= -1:
                self.curr_page = len(self.pages) - 1

        # Returns a list of strings of the images of the gallery items on current page, up to num
        # Can return less items if the number of images on pages is less than num
        def get_images(self, num: int):
            to_return = []
            i = 0
            num = min(len(self.pages[self.curr_page].images), num)
            for i in range(num):
                to_return.append(self.pages[self.curr_page].images[i].image)
            return to_return

        # Returns the image at index of page (current page by default)
        def get_image(self, index: int, page: int = -1):
            if page == -1:
                page = self.curr_page
            return self.pages[page].images[index].image

    gallery = CustomGallery()

    ace_gallery_page = CustomGalleryPage()
    ace_gallery_page.add_image(CustomGalleryImage("images/gallery/lemon01-md.jpg"))
    ace_gallery_page.add_image(CustomGalleryImage("images/gallery/lemon01-md.jpg"))
    ace_gallery_page.add_image(CustomGalleryImage("images/gallery/lemon01-md.jpg"))
    ace_gallery_page.add_image(CustomGalleryImage("images/gallery/lemon01-md.jpg"))
    ace_gallery_page.add_image(CustomGalleryImage("images/gallery/lemon01-md.jpg"))
    
    gallery.add_page(ace_gallery_page)
    gallery.add_page(CustomGalleryPage())
    gallery.add_page(CustomGalleryPage())
    gallery.add_page(CustomGalleryPage())
    gallery.add_page(CustomGalleryPage())
    gallery.add_page(CustomGalleryPage())


init python:
    gallery_hover = [False for i in range(3 * 2)]

screen gallery:
    tag menu

    key "K_ESCAPE" action Return(None)

    add "gui/gallery/BD_Gallery_BG.png"

    # Stacks page
    vbox:
        xsize 1780
        xalign 0.5
        yoffset 64
        # holds top pagebuttons
        hbox:
            xalign 0.5
            imagebutton:
                idle "gui/gallery/BD_GalleryButtons_ace.png"
                hover "gui/gallery/BD_GalleryButtons_aceh.png"
                action Function(gallery.change_page, 0)

            imagebutton:
                idle "gui/gallery/BD_GalleryButtons_ant.png"
                hover "gui/gallery/BD_GalleryButtons_anth.png"
                action Function(gallery.change_page, 1)
            
            imagebutton:
                idle "gui/gallery/BD_GalleryButtons_kale.png"
                hover "gui/gallery/BD_GalleryButtons_kaleh.png"
                action Function(gallery.change_page, 2)

            imagebutton:
                idle "gui/gallery/BD_GalleryButtons_xaea.png"
                hover "gui/gallery/BD_GalleryButtons_xaeah.png"
                action Function(gallery.change_page, 3)

            imagebutton:
                idle "gui/gallery/BD_GalleryButtons_blair.png"
                hover "gui/gallery/BD_GalleryButtons_blairh.png"
                action Function(gallery.change_page, 4)
            
            imagebutton:
                idle "gui/gallery/BD_GalleryButtons_extras.png"
                hover "gui/gallery/BD_GalleryButtons_extrash.png"
                action Function(gallery.change_page, 5)

        # grid for the gallery frames
        $ images = gallery.get_images(6)
        grid 3 2:
            xspacing -80
            yspacing -100
            yoffset -10
            xalign 0.5
            for i in range(6):
                if i < len(images):
                    # do button
                    $img = str(images[i])
                    button:
                        focus_mask True
                        xalign 0.5
                        yalign 0.5
                        hovered SetDict(gallery_hover, i, True)
                        unhovered SetDict(gallery_hover, i, False)

                        action ShowMenu("cg_screen", img)

                        fixed:
                            xmaximum 592
                            ymaximum 433
                            if (gallery_hover[i] == True):
                                add "gui/gallery/BD_Gallery_Slot_BigH.png":
                                    xalign 0.5
                                    yalign 0.5
                            else:
                                add "gui/gallery/BD_Gallery_Slot_Big.png":
                                    xalign 0.5
                                    yalign 0.5


                            add "[img]":
                                xalign 0.5
                                yalign 0.5
                                xsize 486
                                ysize 326

                            if (gallery_hover[i] == True):
                                add "gui/gallery/BD_Gallery_Slot_BigH_Frame.png":
                                    xalign 0.5
                                    yalign 0.5
                            else:
                                add "gui/gallery/BD_Gallery_Slot_Big_Frame.png":
                                    xalign 0.5
                                    yalign 0.5

                else:
                    # empty frame
                    fixed:
                        xmaximum 605
                        ymaximum 453
                        xalign 0.5
                        yalign 0.5
                        add "gui/gallery/BD_Gallery_Slot_Big.png":
                            xalign 0.5
                            yalign 0.5
        
        # bottom nav buttons
        hbox:
            yoffset -45
            yalign 1.0
            xoffset 1188
            spacing 340
            imagebutton:
                idle "gui/gallery/BD_GallerySwitch_L.png"
                hover "gui/gallery/BD_GallerySwitch_LHover.png"
                action Function(gallery.decrement_page)
            imagebutton:
                idle "gui/gallery/BD_GallerySwitch_R.png"
                hover "gui/gallery/BD_GallerySwitch_RHover.png"
                action Function(gallery.increment_page)

screen cg_screen(img):
    tag menu
    key "K_ESCAPE" action ShowMenu("gallery")

    add img

    

    

