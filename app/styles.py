from app.board import background_png
from ecosys import *

checked_img = os.path.join(BASE_DIR,'app','settings','imgs','checked.png')
unchecked_img = os.path.join(BASE_DIR,'app','settings','imgs','unchecked.png')
fold_img =  os.path.join(BASE_DIR,'app','settings','imgs','fold.png')
expand_img =  os.path.join(BASE_DIR,'app','settings','imgs','expand.png')

main_win_style = """
    QMainWindow{
        font: 22px;
        background-color:rgba(255,255,255,0);
        border-image:url('""" + background_png + """');
        }
    """
info_win_style = """  
    QLabel{
        font: 24px bold black;
        border-radius: 5px;
        background-color:rgba(255,255,255,95);
        }
    """
tool_box_style = """ 
    QWidget {
        font:24px;
        background-color:rgba(0,255,255,0);
    } """
    
program_tree = """  
    QTreeView::branch:open:has-children:!has-siblings {}
    QTreeView::branch:open:has-children:has-siblings {image: url('""" + fold_img + """');}
    QTreeView::branch:closed:has-children:!has-siblings{}
    QTreeView::branch:closed:has-children:has-siblings {image: url('""" + expand_img + """');}
    """
pb_message_style = ("""
                QProgressBar{
                    border-radius: 5px;
                    background-color:rgba(200,200,200,0);
                }
                QProgressBar::chunk {
                    background-color:rgba(200,200,200,0);
                }

                QWidget{
                    font:18px;
                    background-color:rgba(200,200,200,0)
                    }
                QFrame{
                    font:18px;
                    background-color:rgba(200,200,200,0)
                }
                 """)

frame_widget_style = """
    QTextBrowser {
        background-color:rgba(255,255,255,0);
    }
    QFrame {
        border-radius: 5px;
        background-color:rgba(255,255,255,0);
    }

 """
main_tab_widget_style=(""" 
    QTabWidget::tab-bar { 
        alignment: center; 
    } 
    QTabBar::tab{
        font:28px;
        width:200px;
        height:60;
        margin-top:5px; 
        margin-right:1px;
        margin-left:1px;
        margin-bottom:0px;
        border-bottom-color: #C2C7CB;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
    }
    QTabWidget::pane{
        border:none;
        }
    QTabBar::tab:!selected {
        color:#606060;
        background:rgba(135,206,250,60);
        }
    QTabBar::tab:hover {
        color:#000000;
        background:rgba(135,206,250,90);
        }
    QTabBar::tab:selected {
        color:#000000;
        background:rgb(135,206,250);
    }
 """)
	# border-image: url(:/common/images/common/左_normal.png);
    # border-image: url(:/common/images/common/左_pressed.png);

wax = "rgba(246, 179, 127,70)"
xyl = "rgba(0, 239, 255,70)"
eth = "rgba(126,206,244,70)"
fml = "rgba(132,204,201,70)"

def get_style(b_color:str):
    _style = (f"""QLabel {{
                font:24px;
                min-width:70px;
                min-height:180px;
                max-width:70px;
                max-height:150px;
                background:{b_color};
                border:1px solid black;
                border-top:1px solid black;
                border-bottom-left-radius:8px;
                border-bottom-right-radius:8px;
                color:black;
                }}""")
    return _style 

wax_style = get_style(wax)
xyl_style = get_style(xyl)
eth_style = get_style(eth)
fml_style = get_style(fml)

label_font = (""" QFont{
                    font:24px;
            }"""
            )


progress_page =(""" 
    QWidget {
        border:1px solid white;
        border-radius:10px;
        }
    QFont{
        color:white;
        border:0px;
        }
    QProgressBar {
        border: 2px solid white;
        border-radius: 10px;
        background: transparent;
        text-align: right;
        width: 20px;
    }        
    QProgressBar::chunk {
        background-color: green;
        }
 """)

caption_button_style =(""" QPushButton{
                        height:30px;
                        width:70px;
                        font:24px bold black;
                        text-align:center middle;
                        border-radius:4px;
                        border: 1px solid #4fa9aD;
                        } 
                    QPushButton:hover{
                        border: 2px solid #4fa9aD;
                        background-color:rgba(200,255,180,50);
                        }
                    QPushButton:pressed{
                        background-color:rgb(225,225,225);
                        }
                    QPushButton:focus{
                        outline:none;
                        }
                                """)
message_style = ("""
                
                QWidget{
                    font:24px;
                    }
                QFrame{
                    font:24px;
                }
                 """)

round_frame_style = (""" 
                QFrame{
                    border: 1px solid #4fa9aD;
                    border-radius:10px;
                }
                """)

button_style =(""" QPushButton{
                        height:40px;
                        width:140px;
                        font:24px bold black;
                        text-align:center middle;
                        border-radius:10px;
                        border: 1px solid #4fa9aD;
                        } 
                    QPushButton:hover{
                        border: 2px solid #4fa9aD;
                        background-color:rgba(40,200,60,70);
                        }
                    QPushButton:pressed{
                        background-color:rgb(225,225,225);
                        }
                    QPushButton:focus{
                        outline:none;
                        }
                    QPushButton:checked

                        {

                        background-color:rgb(255,235,181);

                        }
                                """)
invisible = (""" QWidget{
                qproperty-visible:false;
            } """)
visible = (""" QWidget{
                qproperty-visible:false;
            } """)

vessel_shape = (""" QPushButton{
                font: 30px;
                width: 70px;
                height:30px;
                border-bottom-left-radius:1px;
                border-bottom-right-radius:1px;
                border-top-left-radius:8px;
                border-top-right-radius:8px;
                background-color:#00bfff;
                border:1px solid #1E90FF;
            } """)


time_bar = (""" 
                QWidget {
                    border: 1px solid gray;
                    border-radius: 10px;
                }
                QLabel {
                    font:24px;
                    text-align: center middle;
                    width:40px;
                    height:none;
                    border: 0px solid gray;
                    border-radius: 5px;}
                QFont {font:30px;}
                QProgressBar {
                    border: 1px solid gray;
                    border-radius: 10px;
                    background: transparent;
                    width: 20px;
                }
                QProgressBar::chunk {
                    background-color: rgb(0,255,127);
                    border-radius:10px;
                } """)

time_bar_red = (""" 
                QFont {font:30px;}
                QProgressBar {
                    border: 0px solid red;
                    border-radius: 10px;
                    background: transparent;
                    text-align: center;
                    width: 20px;
                }

                QProgressBar::chunk {
                    background-color: rgb(255,69,0);
                    border-radius:10px;
                } """)

start_bar =(""" 
            QProgressBar {
                font: 15px;
                border: 2px solid grey;
                border-radius: 10px;
                width: 15px;
                text-align: right;
            }

            QProgressBar::chunk {
                background-color: #1E90FF;
                border-radius: 10px;
                width: 15px;
            } """)

motion_view_style = (""" 
            QWidget {font:24px;}
            """)





scroll_vertical= (""" 
    QScrollBar:horizontal {height:60px;background:rgba(100,180,200,12);margin: 0px 0 0px 0;padding-left:60px; padding-right:60px;border-radius:10px;}
    QScrollBar::handle:horizontal{height:60px;background:gray;border-radius:1px;min-width:20px;}
    QScrollBar::add-line:horizontal{height:60px;width:60px;subcontrol-position:right}
    QScrollBar::sub-line:horizontal{height:60px;width:60px;subcontrol-position:left;}
    QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {background:rgba(189,189,189,30);border-radius:1px;}
    """)

others ="""
// QScrollBar::handle:horizontal:hover{height:50px;background:rgba(0,0,0,50%);border-radius:4px;min-width:20;}
 """