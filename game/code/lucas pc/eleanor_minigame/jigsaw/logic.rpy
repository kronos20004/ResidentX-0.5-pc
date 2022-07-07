init python:
    import random

    class Timer(renpy.store.object):
        def __init__(self, ended=0, started=100, passed=0, paused=False):
            self._ended = ended
            self._started= started
            self._current = self._started - passed
            self._passed = passed
            self._paused = paused
            self._over = False
        
        @property
        def ended(self):
            return self._ended
        
        @property
        def started(self):
            return self._started
        
        @property
        def current(self):
            return self._current
        
        @property
        def is_paused(self):
            return self._paused
        
        @property
        def is_over(self):
            return self._over
        
        def restart(self):
            self._current = self._started - self._passed
            self.set_over(False)
            self.start()
        
        def start(self):
            self._paused = False
        
        def pause(self):
            self._paused = True
        
        def set_current(self, value):
            if value > self.started:
                self._started = value
            self._current = max(min(value, self.started), self.ended)
        
        def set_over(self, value):
            self._over = value
        
        def decrement(self, value):
            self._current = max(min(self.current - value, self.started), self.ended)
            
            if self.current == self.ended:
                self.set_over(True)
                self.pause()
        
        def tick(self, value=1):
            if self.is_paused or self.is_over:
                return
            
            self.decrement(value)
            renpy.restart_interaction()


    class JigSaw(renpy.store.object):
        """
            JigSaw("minigame_art01_block01", 9, Timer(0, 16))
            `file_init_name`
                filename without `.png` suffix and (01, 02 and etc. of counter)
            `quantity_files`
                :)
            `valid_image`
                list of right parts of the image - [1, 3, 2, 8 and etc.]. But if parts is linear - [1, 2, 3, 4 and etc.] this can be skipped
            `cell/row`
                cell/row of grid image
            `xsize/ysize`
                xsize/ysize of grid image
            `img_format`
                format of images (webp, jpg and etc.)
        """
        def __init__(
            self, file_init_name, quantity_files, timer,
            valid_image=[], cell=3, row=3, xsize=227, ysize=227,
            img_format=".png"
        ):
            self.file_init_name = file_init_name
            self.quantity_files = quantity_files
            self.current_image = [None] * self.quantity_files
            self.valid_image = valid_image if valid_image else [_ for _ in xrange(1, self.quantity_files+1)]
            self.timer = timer
            self.cell = cell
            self.row = row
            self.xsize = xsize
            self.ysize = ysize
            self.img_format = img_format
            self.queue = [_ for _ in xrange(1, self.quantity_files+1)]
            self.generate_right_position()
            random.shuffle(self.queue)
            self.generate_left_positions()
            self.drags = []
        
        def generate_left_positions(self):
            """ Generate mesh of default positions. """
            self.left_positions = []
            for y in xrange(self.cell):
                for x in xrange(self.row):
                    self.left_positions.append([x*self.xsize, y*self.ysize])
        
        def generate_right_position(self):
            """ Generate valid positions of jigsaw. """
            self.right_positions = []
            for y in xrange(self.cell):
                for x in xrange(self.row):
                    self.right_positions.append([905+x*self.xsize, 75+y*self.ysize])
        
        @property
        def files(self):
            """ Return list of files in img format. """
            return [self.file_init_name + "{0:02}{1}".format(file, self.img_format) for file in self.queue]
        
        def get_index_from_filename(self, search_file):
            """ Slice filename and find in valid_image value and return index. """
            search_file = int(search_file.split(self.img_format)[0][-2:])
            for inx, value in enumerate(self.valid_image):
                if value == search_file:
                    return inx
        
        def get_pseudo_index_from_filename(self, search_file):
            """ Return index of filename in files. """
            for inx, filename in enumerate(self.files):
                if search_file == filename:
                    return inx
        
        @property
        def is_valid(self):
            """ Return collected picture is valid or no."""
            return self.current_image == self.valid_image
        
        def is_valid_position(self, x, y, inx):
            """ Return occurrences position in valid_positions"""
            if not (self.right_positions[inx][0]-self.xsize/3 <= x <= self.right_positions[inx][0]+self.xsize):
                return
            if not (self.right_positions[inx][1]-self.ysize/6 <= y <= self.right_positions[inx][1]+self.ysize):
                return
            return True
        
        def droppable(self, drags, drop):
            index = self.get_index_from_filename(drags[0].drag_name)
            pseudo_index = self.get_pseudo_index_from_filename(drags[0].drag_name)
            if drags[0] not in self.drags:
                self.drags.append(drags[0])  
            if self.is_valid_position(drags[0].x, drags[0].y, index):
                self.current_image[index] = index + 1  
                drags[0].draggable = False  
                drags[0].snap(self.right_positions[index][0], self.right_positions[index][1], .3)  
            else:
                drags[0].target_x, drags[0].target_y = self.left_positions[pseudo_index]  
            renpy.restart_interaction()
        
        def restart(self):
            self.current_image = [None] * self.quantity_files
            for drag in self.drags:
                pseudo_index = self.get_pseudo_index_from_filename(drag.drag_name)
                drag.draggable = True
                drag.snap(self.left_positions[pseudo_index][0], self.left_positions[pseudo_index][1], 1.5)
            self.drags = []
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
