import numpy as np

class MData():
    def __init__(self, parent) -> None:
        super(self).__init__(parent)
        self.fname = None
        self.eventsig = None

    def getoffset(self):
        header_index = 0
        data = np.fromfile(self.fname, dtype=np.uint32)
        for i in range(0, len(data)):
            if(data[i] == self.eventsig):
                header_index = i
                break
        if(i == len(data) - 1):
            header_index = 0
            tfname = self.fname
            self.field_fname.setText(
                "WARNING: ThIs FiLe Do NoT CoNtAiN PrOpEr HeAdEr")
            self.field_fname.setStyleSheet(
                "color: black;  background-color: red")
            self.fname = tfname
        return(header_index)

    def loaddata(self):
        """
        Get the data in the form of array of 48x40 (2d array)(48 channel column, and 40 rows which are samples)
        """
        # GET OFFSET
        self.field_fname.setStyleSheet(
            "color: black;  background-color: white")
        offset = self.getoffset()
        # offset = 0
        print(offset)

        tdata = np.core.records.fromfile(
            self.fname, formats='(48)int32,(40,48)int32', names='header,data', offset=offset * 4)

        tdata = tdata['data']
        tdata = tdata.transpose(0, 2, 1)
        tdata = tdata // (2**8)
        tdata = 20 * tdata / (2**24)
        self.data = tdata
        self.updateall()
        self.value_totevt.setText(str(len(self.data)))
        self.getarea()
        return(self.data)

    def updateall(self):
        if self.data is not None:
            self.updatexy()
            self.updaterangeplot()
            self.updatenoisehistogram()
            self.updatestackplot()

    def updatexy(self):
        if self.data is not None:
            tevtdata = self.data[self.evtno]
            tchndata = tevtdata[self.chan]
            self.x = np.arange(len(tchndata))
            self.x = self.x * self.tbinwidth
            self.y = tchndata
            self.p1.setData(x=self.x, y=self.y)

    def updaterangeplot(self):
        self.getlims()
        # self.ry = self.data[self.lims[0]:self.lims[1],self.chan].flatten()
        self.ry = self.data[0:20, self.chan].flatten()
        self.rx = np.arange(len(self.ry))
        self.p3.setData(x=self.rx, y=self.ry)

    def updatenoisehistogram(self):
        meandata = self.data.mean(axis=2)
        counts, edges = np.histogram(meandata[:, self.chan], bins=self.bins)
        self.hy, self.hx = counts, edges
        self.p2.setData(self.hx, self.hy)

    def updatefname(self):
        self.fname = self.field_fname.text()

    def getlims(self):
        templims = self.value_lims.text().split(sep=",")
        if(len(templims) == 2):
            self.lims = [int(float(i)) for i in templims]
            if(self.lims[1] > len(self.data)):
                self.lims[1] = len(self.data) - 2
        if(len(self.lims) == 2):
            self.evtno = self.lims[0]
            self.updatexy()

    def updatestackplot(self):
        self.getlims()
        # print(self.lims)
        self.sy = self.data[self.lims[0]:self.lims[1], self.chan].flatten()
        self.sx = np.tile(np.arange(0, len(self.data[0, self.chan])), len(
            self.data[self.lims[0]:self.lims[1], self.chan]))
        self.sx = self.sx * self.tbinwidth
        self.p4.setData(x=self.sx, y=self.sy)
        tmean = self.data[self.lims[0]:self.lims[1], self.chan].mean(axis=0)
        self.my = tmean
        self.mx = np.arange(0, len(self.data[0, self.chan]))
        # print(self.my)
        self.p5.setData(x=self.mx * self.tbinwidth, y=self.my)

    def getarea(self):
        if self.data is not None:
            talldata = self.data[:, self.chan].flatten()

            # print(talldata.sum())
            self.value_totarea.setText(str(talldata.sum()))

    def runfreerun(self):
        if self.button_freerun.isChecked():
            self.timer.timeout.connect(self.randxy)
            self.timer.start(2000)
        else:
            self.timer.stop()

    def randxy(self):
        if self.data is not None:
            datalen = len(self.data)
            self.evtno = np.random.randint(datalen)
            self.value_evtno.setText(str(self.evtno))
            self.updatexy()

