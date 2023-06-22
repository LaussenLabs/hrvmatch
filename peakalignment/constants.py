match_window_size = 20
matches_per_window = 1
density_time_step_size = 10
density_time_steps_per_window = 10
density_offset_step_dur_ms = 5
density_offset_steps_per_window = 10
coarse_density_bin_size_ms = 1
coarse_density_accepted_distance_from_max_ms = 60 * (10 ** 3)
max_lines = 10
# residual_threshold = 10_000_000  # Nano
residual_threshold_ms = 10
max_trials = 10_000_000
min_line_inliers = 20
# min_slope = -100_000 / (10 ** 6)
# max_slope = 100_000 / (10 ** 6)
min_slope = 200 / (10 ** 6)
max_slope = 700 / (10 ** 6)
min_inlier_density_ms = 0.05 / (10 ** 3)