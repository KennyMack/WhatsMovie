from forms.principal_design import frmPrincipal

class viewPrincipal(frmPrincipal):
    """docstring forviewPrincipal."""
    def __init__(self):
        super(viewPrincipal, self).__init__()
        self.btnSearch.bind("<Button-1>", self.btnSearch_click)

    def btnSearch_click(self, event):
        print(self.txtWhichMovie.get())
