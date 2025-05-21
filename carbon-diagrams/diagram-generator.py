from PIL import Image, ImageDraw
import math
import random

def check_collision(x, y, positions, min_distance):
    # Check if a new particle position collides with existing ones
    for pos in positions:
        dx = x - pos[0]
        dy = y - pos[1]
        if math.sqrt(dx*dx + dy*dy) < min_distance:
            return True
    return False

def create_atom_diagram(protons, neutrons, size=400, filename="carbon.png"):
    # Initialize transparent canvas
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    center_x = size // 2
    center_y = size // 2
    nucleus_radius = size // 6
    base_particle_radius = size // 22
    
    # Visual settings for particles
    proton_color  = (255, 180, 180)  # Proton: Light red
    neutron_color = (180, 180, 255)  # Neutron: Light blue
    border_color  = (100, 100, 100)  # Particle border: Dark gray
    
    positions = []
    
    def get_valid_position(is_proton):
        max_attempts = 200
        min_distance = base_particle_radius * 2.2
        
        # Divide the nucleus into sectors
        sector_size = nucleus_radius / 3
        
        for attempt in range(max_attempts):
            # Use polar coordinates for better distribution
            if attempt < max_attempts // 2:
                # Try inner and middle regions first
                distance = random.uniform(sector_size, 2 * sector_size)
            else:
                # Try outer region if inner attempts fail
                distance = random.uniform(0, nucleus_radius * 0.9)
            
            angle = random.uniform(0, 2 * math.pi)
            
            # Add slight bias for protons/neutrons to group together
            if is_proton:
                angle += random.uniform(-math.pi/4, math.pi/4)
            
            x = center_x + (distance * math.cos(angle))
            y = center_y + (distance * math.sin(angle))
            
            if not check_collision(x, y, positions, min_distance):
                return x, y
        
        # Fallback position with increased radius if all attempts fail
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, nucleus_radius)
        return (center_x + distance * math.cos(angle),
                center_y + distance * math.sin(angle))

    # Draw protons first, then neutrons
    for is_proton in [True, False]:
        particle_count = protons if is_proton else neutrons
        for _ in range(particle_count):
            x, y = get_valid_position(is_proton)
            positions.append((x, y))
            
            particle_radius = base_particle_radius * random.uniform(0.95, 1.05)
            color = proton_color if is_proton else neutron_color
            
            # Add slight transparency to the particles
            color = color + (230,)  # Add alpha channel
            border_color_alpha = border_color + (255,)  # Solid border
            
            draw.ellipse([x - particle_radius, y - particle_radius,
                         x + particle_radius, y + particle_radius],
                        fill=color, outline=border_color_alpha)
    
    img.save(filename)

# Generate isotope diagrams
create_atom_diagram(6, 6, filename="carbon-12.png")
create_atom_diagram(6, 7, filename="carbon-13.png")
create_atom_diagram(6, 8, filename="carbon-14.png")