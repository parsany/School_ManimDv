from manim import *
import numpy as np


config.frame_rate = 60
config.pixel_height = 1080
config.pixel_width = 1920

class DerivativePresentation(Scene):
    def construct(self):
        
        self.show_title_slide()

        
        self.show_definition_slide()

        
        self.show_car_speed_slide()

        
        self.show_limit_definition_slide()

        
        self.show_derivative_animation()

    def show_title_slide(self):
        title = Text("Understanding Derivatives", font_size=72, color=BLUE)
        subtitle = Text("Parsa Niavand", font_size=48, color=WHITE).next_to(title, DOWN)

        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=2)
        self.wait(3)
        self.play(FadeOut(title), FadeOut(subtitle))

    def show_definition_slide(self):
        title = Text("", font_size=48).to_edge(UP)
        graph = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"include_numbers": True}
        )
        point1 = Dot(graph.c2p(2, 3), color=RED)
        point2 = Dot(graph.c2p(6, 7), color=BLUE)
        line = Line(point1.get_center(), point2.get_center(), color=YELLOW)

        formula = MathTex(
            r"\text{Slope} = \frac{y_2 - y_1}{x_2 - x_1}",
            font_size=48
        ).to_corner(UR)

        self.play(Write(title))
        self.play(Create(graph))
        self.play(FadeIn(point1, point2))
        self.play(Create(line))
        self.play(Write(formula))
        self.wait(2)

        
        self.play(formula.animate.set_color(YELLOW))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(graph), FadeOut(formula), FadeOut(line), FadeOut(point1), FadeOut(point2))

    def show_car_speed_slide(self):
        title = Text("Real-World Example: Car Speed", font_size=48, color=BLUE).to_edge(UP)
        car = SVGMobject("car.svg").scale(0.5).to_edge(LEFT)

        self.play(Write(title))
        self.play(FadeIn(car, shift=RIGHT))
        
        
        self.play(car.animate.shift(RIGHT * 10), run_time=5)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(car))

    def show_limit_definition_slide(self):
        title = Text("Limits for derivative", font_size=48, color=BLUE).to_edge(UP)
        definition = MathTex(
            r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}",
            font_size=48
        ).scale(1.5)

        self.play(Write(title))
        self.play(Write(definition))
        self.wait(3)

        
        self.play(definition[0].animate.set_color(YELLOW), run_time=1)
        self.play(definition[1:].animate.set_color(WHITE), run_time=1)
        self.wait(2)
        self.play(FadeOut(title), FadeOut(definition))


    def show_derivative_animation(self):
        title = Text("Visualizing the Derivative", font_size=48, color=BLUE).to_edge(UP)
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 20, 5],
            tips=False,
            axis_config={"include_numbers": True}
        )

        def f(x):
            return -((np.sin(x - 4) * (x / 4)**0.5 * (x + 3)) + (0.1 * (x - 2)**2 * np.sin(x) + 7) - 15)

        graph = ax.plot(f, x_range=[0, 10], color=BLUE)

        self.play(Write(title))
        self.play(Create(ax), Create(graph), run_time=2)
        self.wait(2)

        
        x = ValueTracker(7.3)
        dx = ValueTracker(2)

        
        dot1 = always_redraw(lambda: Dot(color=GREEN).scale(.8).move_to(ax.c2p(x.get_value(), f(x.get_value()))))
        dot2 = always_redraw(lambda: Dot(color=ORANGE).scale(.8).move_to(ax.c2p(x.get_value() + dx.get_value(), f(x.get_value() + dx.get_value()))))

        
        secant_line = always_redraw(lambda: ax.get_secant_slope_group(
            x=x.get_value(),
            dx=dx.get_value(),
            graph=graph,
            dx_label=r"\Delta{x}",
            dy_label=r"\Delta{y}",
            secant_line_color=YELLOW,
        ))

        
        self.play(FadeIn(dot1), FadeIn(dot2), Create(secant_line))
        self.wait(2)

        
        self.play(dx.animate.set_value(0.1), run_time=4)
        self.wait(2)
        self.play(dx.animate.set_value(1e-9), run_time=4)
        self.wait(2)

        
        self.play(x.animate.set_value(1), run_time=4)
        self.wait()
        self.play(x.animate.set_value(8), run_time=7)
        self.wait()

        
        self.play(FadeOut(dot1), FadeOut(dot2), FadeOut(secant_line), FadeOut(graph), FadeOut(ax), FadeOut(title))
