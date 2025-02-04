def adjust_color(value, color1, color2):
    # Determine whether to use color1 or color2 based on the sign of the value
    if value < 0:
        base_color = color1
    else:
        base_color = color2
    
    # Calculate the lightness factor based on the absolute value of the number
    abs_value = abs(value)
    
    # The lightness_factor is highest when abs_value is close to 0 and decreases with abs_value
    lightness_factor = max(0, 1 - min(abs_value / 50.0, 1))  # Inverse of abs_value, capped at 1
    
    # Convert hex color to RGB (assuming the colors are in hex format, e.g., #800080)
    base_rgb = [int(base_color[i:i+2], 16) for i in (1, 3, 5)]
    
    # Lighten the color by blending it with white (255, 255, 255) based on the lightness_factor
    lightened_rgb = [int(c + (255 - c) * lightness_factor) for c in base_rgb]
    
    # Convert the lightened RGB back to hex format
    lightened_hex = '#' + ''.join([f'{c:02x}' for c in lightened_rgb])
    
    return lightened_hex

# Example usage:
color2 = "#9474DE"  # Purple
color1 = "#88C4E0"  # Blue
value = 19.3

result_color = adjust_color(value, color1, color2)
print(f'Resulting color: {result_color}')
