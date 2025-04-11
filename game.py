import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class GameUI:
    def __init__(self, master):
        self.master = master
        master.title("Silicon Strategy")
        
        # Set window size
        master.geometry("800x600")
        
        # Initialize game variables
        self.profit = 100
        self.public_opinion = 100
        self.morale = 100
        self.current_question = 0
        
        # Load game questions
        self.load_questions()
        
        # Start with home page
        self.show_home_page()
    
    def load_questions(self):
        """Define questions with three-part score changes."""
        self.questions = [
            {
                "question": "Should we replace our employees with AI kiosks?",
                "options": {
                    "A": {
                        "text": "Replace all employees",
                        "score_change": {"profit": 50, "public_opinion": -20, "morale": -30},
                        "explanation": "You replaced all employees. Profit soared, but worker morale suffered."
                    },
                    "B": {
                        "text": "Implement an AI chatbot",
                        "score_change": {"profit": 10, "public_opinion": -100, "morale": -10},
                        "explanation": "You introduced a chatbot. Employees are less satisfied."
                    },
                    "C": {
                        "text": "Keep the current system",
                        "score_change": {"profit": 0, "public_opinion": 0, "morale": 10},
                        "explanation": "You made no changes. A safe approach."
                    }
                }
            },
            {
                "question": "Use AI to track customer behavior in-store?",
                "options": {
                    "A": {
                        "text": "Yes, with no privacy measures",
                        "score_change": {"profit": 10, "public_opinion": -30, "morale": 0},
                        "explanation": "Customers felt spied on, hurting public opinion."
                    },
                    "B": {
                        "text": "Yes, with strict privacy controls",
                        "score_change": {"profit": 5, "public_opinion": 10, "morale": 0},
                        "explanation": "You gained insights while respecting privacy."
                    },
                    "C": {
                        "text": "No, avoid AI tracking",
                        "score_change": {"profit": 0, "public_opinion": 0, "morale": 0},
                        "explanation": "You avoided controversy, but gained little insight."
                    }
                }
            },
            {
                "question": "Automate inventory management with AI robots?",
                "options": {
                    "A": {
                        "text": "Fully automate",
                        "score_change": {"profit": 40, "public_opinion": 0, "morale": -40},
                        "explanation": "Automation boosts efficiency significantly but workers feel threatened."
                    },
                    "B": {
                        "text": "Partially automate",
                        "score_change": {"profit": 15, "public_opinion": 0, "morale": -5},
                        "explanation": "A balanced approach, mixing technology with human input."
                    },
                    "C": {
                        "text": "Keep manual process",
                        "score_change": {"profit": 0, "public_opinion": 0, "morale": 5},
                        "explanation": "You missed some efficiency gains, but employees feel secure."
                    }
                }
            }
        ]
    
    def clear_screen(self):
        """Clear all widgets from the screen."""
        for widget in self.master.winfo_children():
            widget.destroy()
    
    def show_home_page(self):
        """Display the home page with start button."""
        self.clear_screen()
        
        # Load the home background image
        image_path = os.path.join("assets", "home.jpg")
        self.home_bg_image = Image.open(image_path)
        # Resize the image to fit the window
        self.home_bg_image = self.home_bg_image.resize((800, 600), Image.LANCZOS)
        self.home_bg_photo = ImageTk.PhotoImage(self.home_bg_image)
        
        # Create a canvas to display the background image
        self.home_canvas = tk.Canvas(self.master, width=800, height=600)
        self.home_canvas.pack(fill="both", expand=True)
        self.home_canvas.create_image(0, 0, image=self.home_bg_photo, anchor="nw")
        
        # Create start game button
        start_button = tk.Button(
            self.master,
            text="Start Game",
            command=self.show_instructions,
            font=("Helvetica", 18),
            bg="#4CAF50",
            fg="white",
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=10
        )
        start_button_window = self.home_canvas.create_window(425, 540, window=start_button)
    
    def show_instructions(self):
        """Display game instructions."""
        self.clear_screen()
        
        # Keep using the home background
        self.instructions_canvas = tk.Canvas(self.master, width=800, height=600)
        self.instructions_canvas.pack(fill="both", expand=True)
        self.instructions_canvas.create_image(0, 0, image=self.home_bg_photo, anchor="nw")
        
        # Create a semi-transparent box for instructions
        instruction_frame = tk.Frame(
            self.master,
            bg="#333333",
            bd=2
        )
        instruction_frame.place(x=150, y=100, width=500, height=400)
        
        # Instructions title
        instructions_title = tk.Label(
            instruction_frame,
            text="How to Play",
            font=("Helvetica", 20, "bold"),
            bg="#333333",
            fg="white"
        )
        instructions_title.pack(pady=(20, 10))
        
        # Instructions text
        instructions_text = """
As the CEO of a company implementing AI, you'll make strategic decisions that affect three key performance indicators:

• Profit: Your company's financial health
• Public Opinion: How customers view your company
• Employee Morale: How your workers feel

For each scenario, choose one of three options. Your decision will immediately affect all three scores.

If any score drops below zero, you lose the game!

Balance all three factors carefully - prioritizing profit alone may hurt your reputation and employee satisfaction. Your final score
is calculated as an average of all 3 factors.

Make wise choices and lead your company to success in the AI era!
        """
        
        instructions_label = tk.Label(
            instruction_frame,
            text=instructions_text,
            font=("Helvetica", 12),
            bg="#333333",
            fg="white",
            justify="left",
            wraplength=460
        )
        instructions_label.pack(padx=20, pady=10)
        
        # Start button
        start_button = tk.Button(
            instruction_frame,
            text="Start",
            command=self.start_game,
            font=("Helvetica", 16),
            bg="#4CAF50",
            fg="black",
            padx=30,
            pady=5
        )
        start_button.pack(pady=5)
    
    def start_game(self):
        """Start the actual gameplay."""
        self.clear_screen()
        
        # Reset game values
        self.profit = 100
        self.public_opinion = 100
        self.morale = 100
        self.current_question = 0
        
        # Load the gameplay background image
        image_path = os.path.join("assets", "questions.jpg")
        self.bg_image = Image.open(image_path)
        # Resize the image to fit the window
        self.bg_image = self.bg_image.resize((800, 600), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Create a canvas to display the background image
        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        
        # Create text widgets for question and options
        self.question_text = self.canvas.create_text(
            400, 40,  # Position in the top box (moved up from 100)
            text="",
            font=("Helvetica", 16, "bold"),
            fill="black",
            width=600,
            justify="center"
        )
        
        # Create text widgets for options (these will be used for highlighting only)
        self.option_a_text = self.canvas.create_text(
            400, 0,  # Position in the first lower box
            text="",
            font=("Helvetica", 14),
            fill="black",
            width=500,
            justify="center"
        )
        
        self.option_b_text = self.canvas.create_text(
            400, 350,  # Position in the second lower box
            text="",
            font=("Helvetica", 14),
            fill="black",
            width=500,
            justify="center"
        )
        
        self.option_c_text = self.canvas.create_text(
            400, 450,  # Position in the third lower box
            text="",
            font=("Helvetica", 14),
            fill="black",
            width=500,
            justify="center"
        )
        
        # Create text widgets for KPI tracker (moved to bottom)
        self.profit_text = self.canvas.create_text(
            180, 540,  # Position in the Profitability box at the bottom
            text=f"{self.profit}",
            font=("Helvetica", 24, "bold"),
            fill="black"  # Changed from white to black for better visibility
        )
        
        self.public_opinion_text = self.canvas.create_text(
            620, 540,  # Position in the Customer Satisfaction box at the bottom
            text=f"{self.public_opinion}",
            font=("Helvetica", 24, "bold"),
            fill="black"  # Changed from white to black for better visibility
        )
        
        self.morale_text = self.canvas.create_text(
            390, 540,  # Position in the Employee Morale box at the bottom
            text=f"{self.morale}",
            font=("Helvetica", 24, "bold"),
            fill="black"  # Changed from white to black for better visibility
        )
        
        # Create explanation text
        self.explanation_text = self.canvas.create_text(
            400, 375,  # Position above the KPI tracker
            text="",
            font=("Helvetica", 14),
            fill="red",
            width=700,
            justify="center"
        )
        
        # Create buttons for options with text directly on them
        self.selected_option = tk.StringVar(value="")
        
        self.option_a_button = tk.Button(
            self.master,
            text="",  # Will be set in load_question
            command=lambda: self.select_option("A"),
            font=("Helvetica", 14),
            bg="white",
            fg="black",
            relief=tk.RAISED,
            bd=2,
            width=40,
            height=2
        )
        self.option_a_button.place(x=150, y=120, width=500, height=40)
        
        self.option_b_button = tk.Button(
            self.master,
            text="",  # Will be set in load_question
            command=lambda: self.select_option("B"),
            font=("Helvetica", 14),
            bg="white",
            fg="black",
            relief=tk.RAISED,
            bd=2,
            width=40,
            height=2
        )
        self.option_b_button.place(x=150, y=190, width=500, height=40)
        
        self.option_c_button = tk.Button(
            self.master,
            text="",  # Will be set in load_question
            command=lambda: self.select_option("C"),
            font=("Helvetica", 14),
            bg="white",
            fg="black",
            relief=tk.RAISED,
            bd=2,
            width=40,
            height=2
        )
        self.option_c_button.place(x=150, y=260, width=500, height=40)
        
        # Add a home button for returning to main menu
        self.home_button = tk.Button(
            self.master,
            text="Home",
            command=self.show_home_page,
            font=("Helvetica", 12),
            bg="#555555",
            fg="white",
        )
        self.home_button.place(x=20, y=20, width=80, height=30)
        
        # Load the first question
        self.load_question()
    
    def select_option(self, option):
        """Handle option selection, highlight the chosen option, and process the answer."""
        # Set the selected option
        self.selected_option.set(option)
        
        # Highlight only the selected button
        self.option_a_button.config(bg="white")
        self.option_b_button.config(bg="white")
        self.option_c_button.config(bg="white")
        
        if option == "A":
            self.option_a_button.config(bg="lightblue")
        elif option == "B":
            self.option_b_button.config(bg="lightblue")
        elif option == "C":
            self.option_c_button.config(bg="lightblue")
            
        # Disable controls during the feedback period
        self.option_a_button.config(state=tk.DISABLED)
        self.option_b_button.config(state=tk.DISABLED)
        self.option_c_button.config(state=tk.DISABLED)
        self.home_button.config(state=tk.DISABLED)
        
        # Process the answer
        self.process_answer(option)
        
    def process_answer(self, choice):
        """Process the selected option and update scores."""
        # Get the selected option data
        q = self.questions[self.current_question]
        option = q["options"][choice]
        score_change = option["score_change"]
        
        # Update each score component
        self.profit += score_change["profit"]
        self.public_opinion += score_change["public_opinion"]
        self.morale += score_change["morale"]
        
        # Update KPI tracker
        self.canvas.itemconfig(self.profit_text, text=f"{self.profit}")
        self.canvas.itemconfig(self.public_opinion_text, text=f"{self.public_opinion}")
        self.canvas.itemconfig(self.morale_text, text=f"{self.morale}")
        
        # Show the explanation
        self.canvas.itemconfig(self.explanation_text, text=option["explanation"])
        
        # Check if any score went negative. End the game immediately if so.
        if self.profit < 0 or self.public_opinion < 0 or self.morale < 0:
            messagebox.showinfo("Game Over", "One of the scores dropped below zero. Game Over!")
            self.show_home_page()
            return
            
        # Schedule the next question
        self.current_question += 1
        self.master.after(5000, self.load_question)
        
    def load_question(self):
        """Load a new question or finish the game."""
        if self.current_question >= len(self.questions):
            # Handle end of game
            messagebox.showinfo("Game Complete", f"Game complete!\nFinal score: {round(3 / (1/self.profit + 1/self.public_opinion + 1/self.morale))}")
            self.show_home_page()
            return
            
        # Reset UI state for the new question
        self.selected_option.set("")
        self.canvas.itemconfig(self.explanation_text, text="")
        
        # Reset button colors and enable buttons
        self.option_a_button.config(bg="white", state=tk.NORMAL)
        self.option_b_button.config(bg="white", state=tk.NORMAL)
        self.option_c_button.config(bg="white", state=tk.NORMAL)
        self.home_button.config(state=tk.NORMAL)
        
        # Display the new question
        q = self.questions[self.current_question]
        self.canvas.itemconfig(self.question_text, text=f"{self.current_question + 1}) {q['question']}")
        
        # Update button text
        self.option_a_button.config(text=f"A. {q['options']['A']['text']}")
        self.option_b_button.config(text=f"B. {q['options']['B']['text']}")
        self.option_c_button.config(text=f"C. {q['options']['C']['text']}")
        
        # Update KPI tracker
        self.canvas.itemconfig(self.profit_text, text=f"{self.profit}")
        self.canvas.itemconfig(self.public_opinion_text, text=f"{self.public_opinion}")
        self.canvas.itemconfig(self.morale_text, text=f"{self.morale}")

if __name__ == "__main__":
    root = tk.Tk()
    game = GameUI(root)
    root.mainloop()
