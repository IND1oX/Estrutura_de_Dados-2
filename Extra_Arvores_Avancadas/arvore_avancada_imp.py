import sys
import math
import random
import pygame

# -----------------------------------------------------------------------------
# 1. EFEITOS SONOROS SINTETIZADOS (Sem arquivos externos)
# -----------------------------------------------------------------------------
class SoundEffects:
    @staticmethod
    def play_tone(freq, duration=0.1, volume=0.3):
        """Gera um tom senoidal simples utilizando o Pygame Mixer"""
        sample_rate = 44100
        n_samples = int(sample_rate * duration)
        buf = bytearray()
        for i in range(n_samples):
            t = float(i) / sample_rate
            val = int(127 + 127 * math.sin(2 * math.pi * freq * t))
            buf.append(val)
        try:
            sound = pygame.mixer.Sound(buffer=bytes(buf))
            sound.set_volume(volume)
            sound.play()
        except Exception:
            pass

    @classmethod
    def sound_plant(cls):
        cls.play_tone(440, 0.08, 0.2)

    @classmethod
    def sound_rotate(cls):
        cls.play_tone(880, 0.15, 0.3)

    @classmethod
    def sound_game_over(cls):
        cls.play_tone(150, 0.4, 0.4)

# -----------------------------------------------------------------------------
# 2. SISTEMA DE PARTÍCULAS VISUAIS
# -----------------------------------------------------------------------------
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-3, -1)
        self.color = color
        self.radius = random.uniform(3, 6)
        self.lifetime = random.randint(20, 40)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.radius = max(0, self.radius - 0.1)
        self.lifetime -= 1

    def draw(self, surface):
        if self.lifetime > 0 and self.radius > 0:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))

# -----------------------------------------------------------------------------
# 3. ESTRUTURA DE DADOS: ÁRVORE AVL
# -----------------------------------------------------------------------------
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        
        # Posições para renderização gráfica e animações
        self.x = 0
        self.y = 0
        self.start_x = 0
        self.start_y = 0
        self.target_x = 0
        self.target_y = 0
        self.anim_progress = 1.0

class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert_bst(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert_bst(root.left, key)
        elif key > root.key:
            root.right = self.insert_bst(root.right, key)
        else:
            return root

        self.update_height(root)
        return root

    def rebalance_node(self, root, target_key):
        if not root:
            return root, False

        rotated = False
        if target_key < root.key:
            root.left, rotated = self.rebalance_node(root.left, target_key)
        elif target_key > root.key:
            root.right, rotated = self.rebalance_node(root.right, target_key)
        else:
            balance = self.get_balance(root)

            # Rotação Esquerda-Esquerda
            if balance > 1 and self.get_balance(root.left) >= 0:
                return self.right_rotate(root), True

            # Rotação Esquerda-Direita
            if balance > 1 and self.get_balance(root.left) < 0:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root), True

            # Rotação Direita-Direita
            if balance < -1 and self.get_balance(root.right) <= 0:
                return self.left_rotate(root), True

            # Rotação Direita-Esquerda
            if balance < -1 and self.get_balance(root.right) > 0:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root), True

        self.update_height(root)
        return root, rotated

    def check_unbalanced_nodes(self, node, critical_nodes=None):
        if critical_nodes is None:
            critical_nodes = []
        if node:
            fb = self.get_balance(node)
            if abs(fb) >= 2:
                critical_nodes.append(node)
            self.check_unbalanced_nodes(node.left, critical_nodes)
            self.check_unbalanced_nodes(node.right, critical_nodes)
        return critical_nodes

    def get_rotation_hint(self, node):
        """Retorna dica didática do tipo de rotação necessária"""
        fb = self.get_balance(node)

        if fb > 1:
            if self.get_balance(node.left) >= 0:
                return "Rotação Simples à Direita (LL)"
            else:
                return "Rotação Dupla Esquerda-Direita (LR)"
        elif fb < -1:
            if self.get_balance(node.right) <= 0:
                return "Rotação Simples à Esquerda (RR)"
            else:
                return "Rotação Dupla Direita-Esquerda (RL)"
        return ""

# -----------------------------------------------------------------------------
# 4. GAME ENGINE E INTERFACE GRÁFICA (PYGAME)
# -----------------------------------------------------------------------------
class UniqueTreesGame:
    def __init__(self):
        pygame.init()
        try:
            pygame.mixer.init(frequency=44100, size=-16, channels=1)
        except Exception:
            pass
        
        self.WIDTH, self.HEIGHT = 1000, 750
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Unique Trees: AVL Upgrade - Master Edition")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Lato", 18, bold=True)
        self.title_font = pygame.font.SysFont("Lato", 26, bold=True)
        self.huge_font = pygame.font.SysFont("Lato", 36, bold=True)

        # Cores
        self.COLOR_BG = (40, 44, 52)
        self.COLOR_CANOPY = (30, 32, 38)
        self.COLOR_BRANCH = (120, 100, 80)
        self.COLOR_BALANCED = (76, 175, 80)
        self.COLOR_CRITICAL = (244, 67, 54)
        self.COLOR_TEXT = (255, 255, 255)
        self.COLOR_GOLD = (255, 215, 0)

        # Configuração de Níveis
        self.levels = [
            {"id": 1, "name": "Nível 1: Rotações Simples", "seeds": [10, 5, 2, 15, 20], "timed": False, "max_rotations": 3},
            {"id": 2, "name": "Nível 2: Rotações Duplas", "seeds": [10, 5, 7, 15, 12], "timed": False, "max_rotations": 4},
            {"id": 3, "name": "Nível 3: Modo Pressão (Tempo)", "seeds": [8, 4, 9, 5, 10, 6, 7, 11, 12], "timed": True, "max_rotations": 6}
        ]
        self.current_level_idx = 0
        
        self.TIMER_EVENT = pygame.USEREVENT + 1
        self.particles = []
        self.reset_level()

    def reset_level(self):
        level = self.levels[self.current_level_idx]
        self.avl_tree = AVLTree()
        self.root = None
        self.seed_queue = level["seeds"].copy()
        self.current_seed_idx = 0
        self.rotation_count = 0
        self.game_over = False
        self.game_over_reason = ""
        self.victory = False
        
        if level["timed"]:
            pygame.time.set_timer(self.TIMER_EVENT, 4000)
        else:
            pygame.time.set_timer(self.TIMER_EVENT, 0)

    def check_victory_condition(self):
        """Verifica ativamente se todas as sementes foram plantadas e a árvore está balanceada"""
        if self.current_seed_idx == len(self.seed_queue) and not self.game_over:
            critical_nodes = self.avl_tree.check_unbalanced_nodes(self.root)
            if not critical_nodes:
                self.victory = True

    def spawn_particles(self, x, y, color):
        for _ in range(20):
            self.particles.append(Particle(x, y, color))

    def update_positions(self, node, x, y, dx):
        if not node:
            return
        
        if node.target_x != x or node.target_y != y:
            node.start_x = node.x
            node.start_y = node.y
            node.target_x = x
            node.target_y = y
            node.anim_progress = 0.0

        if node.anim_progress < 1.0:
            node.anim_progress += 0.08
            t = min(1.0, node.anim_progress)
            smooth_t = t * t * (3 - 2 * t)
            node.x = node.start_x + (node.target_x - node.start_x) * smooth_t
            node.y = node.start_y + (node.target_y - node.start_y) * smooth_t
        else:
            node.x = node.target_x
            node.y = node.target_y

        if node.left:
            self.update_positions(node.left, x - dx, y + 70, dx / 1.8)
        if node.right:
            self.update_positions(node.right, x + dx, y + 70, dx / 1.8)

    def draw_tree(self, node):
        if not node:
            return

        if node.left:
            pygame.draw.line(self.screen, self.COLOR_BRANCH, (node.x, node.y), (node.left.x, node.left.y), 4)
            self.draw_tree(node.left)
        if node.right:
            pygame.draw.line(self.screen, self.COLOR_BRANCH, (node.x, node.y), (node.right.x, node.right.y), 4)
            self.draw_tree(node.right)

        fb = self.avl_tree.get_balance(node)
        is_critical = abs(fb) >= 2
        
        if is_critical:
            pulse = (math.sin(pygame.time.get_ticks() * 0.01) + 1) / 2
            color = (244, int(67 + pulse * 100), int(54 + pulse * 100))
        else:
            color = self.COLOR_BALANCED

        pygame.draw.circle(self.screen, color, (int(node.x), int(node.y)), 22)
        pygame.draw.circle(self.screen, (255, 255, 255), (int(node.x), int(node.y)), 22, 2)

        txt = self.font.render(str(node.key), True, self.COLOR_TEXT)
        self.screen.blit(txt, (node.x - txt.get_width() // 2, node.y - txt.get_height() // 2 - 2))

        fb_txt = self.font.render(f"FB:{fb}", True, self.COLOR_GOLD if is_critical else (200, 200, 200))
        self.screen.blit(fb_txt, (node.x - fb_txt.get_width() // 2, node.y + 25))

    def get_clicked_node(self, node, pos):
        """Raio de clique aumentado para 35px para maior facilidade no clique"""
        if not node:
            return None
        mx, my = pos
        if (node.x - mx)**2 + (node.y - my)**2 <= 35**2:
            return node
        left = self.get_clicked_node(node.left, pos)
        if left: return left
        return self.get_clicked_node(node.right, pos)

    def plant_seed(self):
        if self.current_seed_idx >= len(self.seed_queue):
            return

        critical_nodes = self.avl_tree.check_unbalanced_nodes(self.root)
        if critical_nodes:
            self.game_over = True
            self.game_over_reason = "DEGENERAÇÃO! A árvore colapsou por falta de rotação."
            SoundEffects.sound_game_over()
            return

        val = self.seed_queue[self.current_seed_idx]
        self.root = self.avl_tree.insert_bst(self.root, val)
        self.current_seed_idx += 1
        SoundEffects.sound_plant()

        if self.current_seed_idx == 1:
            self.root.x, self.root.y = self.WIDTH // 2, 140
            self.root.start_x, self.root.start_y = self.root.x, self.root.y

        if self.avl_tree.get_height(self.root) > 5:
            self.game_over = True
            self.game_over_reason = "ALTURA EXCEDIDA! O canteiro estourou."
            SoundEffects.sound_game_over()

        self.check_victory_condition()

    def calculate_stars(self):
        max_rot = self.levels[self.current_level_idx]["max_rotations"]
        if self.rotation_count <= max_rot:
            return "⭐⭐⭐"
        elif self.rotation_count <= max_rot + 2:
            return "⭐⭐"
        return "⭐"

    def run(self):
        while True:
            self.screen.fill(self.COLOR_BG)
            mouse_pos = pygame.mouse.get_pos()

            pygame.draw.rect(self.screen, self.COLOR_CANOPY, (50, 90, self.WIDTH - 100, self.HEIGHT - 200), border_radius=12)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == self.TIMER_EVENT and not self.game_over and not self.victory:
                    self.plant_seed()

                if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                    if event.button == 1 and not self.victory:
                        self.plant_seed()

                    elif event.button == 3 and self.root:
                        clicked = self.get_clicked_node(self.root, event.pos)
                        if clicked:
                            self.root, rotated = self.avl_tree.rebalance_node(self.root, clicked.key)
                            if rotated:
                                self.rotation_count += 1
                                SoundEffects.sound_rotate()
                                self.spawn_particles(clicked.x, clicked.y, self.COLOR_GOLD)
                                # Recalcula a vitória imediatamente após a rotação
                                self.check_victory_condition()

                # Controlos do Teclado
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_level()
                    # Tecla N: Passa de nível se venceu ou se pressionado manualmente
                    elif event.key == pygame.K_n:
                        if self.current_level_idx < len(self.levels) - 1:
                            self.current_level_idx += 1
                            self.reset_level()
                    # Tecla P: Volta para o nível anterior
                    elif event.key == pygame.K_p:
                        if self.current_level_idx > 0:
                            self.current_level_idx -= 1
                            self.reset_level()

            if self.root:
                self.update_positions(self.root, self.WIDTH // 2, 140, self.WIDTH // 4.5)
                self.draw_tree(self.root)

            for p in self.particles[:]:
                p.update()
                p.draw(self.screen)
                if p.lifetime <= 0:
                    self.particles.remove(p)

            # HUD
            lvl_info = self.levels[self.current_level_idx]
            title = self.title_font.render(f"{lvl_info['name']}", True, (166, 178, 63))
            self.screen.blit(title, (60, 20))

            controls = "Esq: Plantar | Dir: Rotação | R: Reiniciar | N: Próximo Nível | P: Nível Anterior"
            self.screen.blit(self.font.render(controls, True, (200, 200, 200)), (60, 55))

            stats = f"Rotações: {self.rotation_count} | Sementes: {self.current_seed_idx}/{len(self.seed_queue)}"
            self.screen.blit(self.font.render(stats, True, self.COLOR_TEXT), (self.WIDTH - 300, 20))

            if self.root:
                hovered = self.get_clicked_node(self.root, mouse_pos)
                if hovered and abs(self.avl_tree.get_balance(hovered)) >= 2:
                    hint = self.avl_tree.get_rotation_hint(hovered)
                    tooltip = self.font.render(f"Dica: {hint}", True, self.COLOR_GOLD)
                    pygame.draw.rect(self.screen, (20, 20, 20), (mouse_pos[0] + 10, mouse_pos[1] - 10, tooltip.get_width() + 10, 25), border_radius=5)
                    self.screen.blit(tooltip, (mouse_pos[0] + 15, mouse_pos[1] - 8))

            if self.game_over:
                msg = self.huge_font.render(f"GAME OVER: {self.game_over_reason}", True, self.COLOR_CRITICAL)
                self.screen.blit(msg, (self.WIDTH // 2 - msg.get_width() // 2, self.HEIGHT - 80))
            elif self.victory:
                stars = self.calculate_stars()
                msg = self.huge_font.render(f"VITÓRIA! Avaliação: {stars}", True, self.COLOR_BALANCED)
                self.screen.blit(msg, (self.WIDTH // 2 - msg.get_width() // 2, self.HEIGHT - 90))
                sub_msg = self.font.render("Pressione 'N' para a próxima fase!", True, self.COLOR_TEXT)
                self.screen.blit(sub_msg, (self.WIDTH // 2 - sub_msg.get_width() // 2, self.HEIGHT - 45))

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = UniqueTreesGame()
    game.run()