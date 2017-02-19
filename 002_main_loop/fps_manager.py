import pygame


class FPSManager:
    min_fps = 5
    max_fps = 200
    default_fps = 60

    def __init__(self):
        self._frame_count = 0
        self._fps = self.default_fps
        self._one_frame_time = self.__get_one_frame_time(self.default_fps)
        self._start_tick = self.__get_ticks()
        self._last_tick = self._start_tick

    def set_fps(self, fps):
        if self.min_fps <= fps and self.max_fps >= fps:
            self._framecount = 0
            self._fps = fps
            self._one_frame_time = self.__get_one_frame_time(fps)
            print('new fps set: {} frame time: {}'.format(
                self._fps, self._one_frame_time))
        else:
            print('Invalid FPS!')

    def get_fps(self):
        return self._fps

    def finish_frame(self):
        self._frame_count += 1

        current_time = self.__get_ticks()
        # set time (ticks) passed since the last frame
        time_passed = current_time - self._last_tick
        self._last_tick = current_time
        # calculate the ticks we should have reached now if we don't have slow
        # frames
        target_tick = self._start_tick + \
            (self._frame_count * self._one_frame_time)
        # if we are ahead of time (no slow frame)
        # delay until current_time == target_tick
        if current_time <= target_tick:  # equality is included for the sake of lesser code
            # if we have a lot of time to wait, use the less accurate wait
            if 10 < target_tick - current_time:
                pygame.time.wait(10)
            # do a busy waiting with zero so it's really accurate
            while int(target_tick) > self.__get_ticks():
                pygame.time.delay(0)
        else:
            self._frame_count = 0
            self._start_tick = self.__get_ticks()

        return time_passed

    def __get_one_frame_time(self, fps):
        return 1000.0 / fps

    def __get_ticks(self):
        now = pygame.time.get_ticks()
        if 0 != now:
            return now
        return 1


def test_fps_manager():
    fps_manager = FPSManager()

    print("Trying Invalid settings:")
    fps_manager.set_fps(2)
    assert(FPSManager.default_fps == fps_manager.get_fps())

    fps_manager.set_fps(10000)
    assert(FPSManager.default_fps == fps_manager.get_fps())

    print("Trying valid settings:")
    fps_manager.set_fps(20)
    assert(20 == fps_manager.get_fps())

    fps_manager.set_fps(30)
    assert(30 == fps_manager.get_fps())

if __name__ == "__main__":
    test_fps_manager()
