import flet as ft
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Row,
    Text,
    icons,
)
import settings

def main(page: ft.Page):
    
    ##################################### SETTINGS LOADER ######################################################################
    
    data = settings.load()
    mapTabs = []
    for mapping in data["mappings"] :
        name = mapping["name"]
        source = mapping["sourcePath"]
        destination = mapping["destinationPath"]
        type = mapping["type"]
        format = mapping["format"]

        icon = ft.icons.PHOTO_CAMERA if type=="photo" else ft.icons.MOVIE
        description = "Picture Mapping" if type =="photo" else "Video Mapping"


        mapTabs.append(ft.ExpansionTile(
                title=ft.ListTile(leading=ft.Icon(icon),
                                title=ft.Text(name),
                                trailing=ft.PopupMenuButton(
                                icon=ft.icons.MORE_VERT,
                                    items=[
                                        ft.PopupMenuItem(text="Modify",icon=ft.icons.EDIT),
                                        ft.PopupMenuItem(text="Remove",icon=ft.icons.REMOVE),
                                    ],
                                ),),
                subtitle=ft.Text(description),
                affinity=ft.TileAffinity.LEADING,
                collapsed_text_color=ft.colors.BLUE,
                text_color=ft.colors.BLUE,
                controls=[
                    ft.ListTile(title=ft.Text("Source : "+source)),
                    ft.ListTile(title=ft.Text("Destination : "+destination)),
                    ft.ListTile(title=ft.Text("Format : "+format)),
                ],
            ))


    ############################## FUNCTION FOR MAPPING ADDER ###############################

    def selectedVideo(e) :
        addType = "video"
        wizard.value = "Please insert your SD card and choose the "+addType+" source folder"
        typeWizard.name = ft.icons.MOVIE
        page.update()

    def selectedPhoto(e) :
        addType = "photo"
        wizard.value = "Please insert your SD card and choose the "+addType+" source folder"
        typeWizard.name = ft.icons.PHOTO_CAMERA
        page.update()


    #############################  FILE PICKER   #####################################
    

     # Open directory dialog
    def get_directory_result(e: FilePickerResultEvent):
        if e.path :
            sourcePath = e.path
            wizard.value = "You chose : "+sourcePath+" \nNow choose destination folder"

        else :
            wizard.value = "You've canceled your choice, please try again"
        page.update()

    

    
    ##################################### VARIABLE FOR MAPPING ADDER ################################################

    wizard = ft.Text(value="Please select one")
    typeWizard = ft.Icon()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()
    sourcePath = None
    addType = None



    ############################## APP BAR ##################################################


    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.SD_CARD_SHARP),
        leading_width=40,
        title=ft.Text("sdCatcher"),
        center_title=True,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Settings",icon=ft.icons.SETTINGS),
                    ft.PopupMenuItem(text="Github",icon=ft.icons.WEB),
                    ft.PopupMenuItem(text="Check update",icon=ft.icons.UPDATE),
                ]
            ),
        ],
    )
##################################  TABS              ############################################
    # hide all dialogs in overlay
    page.overlay.extend([get_directory_dialog])

    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="SD Mappings",
                icon=ft.icons.LIST_ALT,
                content=ft.Column(mapTabs),
            ),
            ft.Tab(
                text="Add new Mapping",
                icon=ft.icons.ADD,
                content=ft.Column(
                    [
                        ft.Row([
                            ft.TextButton("Photo Mapping",icon=ft.icons.PHOTO_CAMERA, on_click=selectedPhoto),
                            ft.TextButton(text="Video Mapping",icon=ft.icons.MOVIE, on_click=selectedVideo),
                                ],alignment=ft.MainAxisAlignment.CENTER),
                        typeWizard,
                        ElevatedButton(
                                "Open directory",
                                icon=icons.FOLDER_OPEN,
                                on_click=lambda _: get_directory_dialog.get_directory_path(),
                                disabled=page.web, ),
                        directory_path,
                        wizard,
                                
                    ]
                    
                    
                    )
            ),
        ],
        expand=1,
    )
    
    ############################### BUILD #################################

    page.add(t)
    

ft.app(target=main)