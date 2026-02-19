import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
import time

writer = FFMpegWriter(fps=30)

fig = plt.figure()
with writer.saving(fig, "writer_test.mp4", 100):
    # Fill in 100x100 grid
    # 30 fps * 10 seconds = 300 frames
    num_grid = 100 * 100
    num_frames = 10 * 30
    frame_skip = num_grid // num_frames
    for i, grid_index in enumerate(range(0, num_grid, frame_skip)):
        start = time.time()

        # grid cells to put a marker on
        j = np.arange(0, grid_index+0.5, step=1.0).astype(np.int32)
        x = j % 100
        y = j // 100

        # plt.figure()
        plt.clf()
        plt.scatter(x, y, marker='x')
        plt.xlim((0, 100))
        plt.ylim((0, 100))
        writer.grab_frame()

        end = time.time()
        print(f'frame {i} rendered at {1.0 / (end - start):0.2f} fps')
