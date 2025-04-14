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
        "question": "Should we deploy AI to schedule all employee shifts automatically?",
        "options": {
            "A": {
                "text": "Fully automate scheduling",
                "score_change": {"profit": 25, "public_opinion": -10, "morale": -30},
                "explanation": "Profit rises due to optimized staffing, but employees feel their personal needs are ignored."
            },
            "B": {
                "text": "Use AI to assist managers but allow manual overrides",
                "score_change": {"profit": 10, "public_opinion": 5, "morale": 10},
                "explanation": "A blended approach improves efficiency while maintaining some flexibility for workers."
            },
            "C": {
                "text": "Avoid AI for scheduling",
                "score_change": {"profit": 0, "public_opinion": 0, "morale": 5},
                "explanation": "Workers appreciate the human touch, but scheduling inefficiencies persist."
            }
        }
    },
    {
        "question": "Should we install AI-driven cameras to monitor employee performance in real time?",
        "options": {
            "A": {
                "text": "Install without notifying staff",
                "score_change": {"profit": 15, "public_opinion": -30, "morale": -50},
                "explanation": "Productivity improves, but trust between staff and leadership is severely damaged."
            },
            "B": {
                "text": "Install and communicate clearly with employees",
                "score_change": {"profit": 10, "public_opinion": -5, "morale": -10},
                "explanation": "Transparency softens the blow, but morale still dips."
            },
            "C": {
                "text": "Do not implement the monitoring system",
                "score_change": {"profit": 0, "public_opinion": 10, "morale": 20},
                "explanation": "Employees feel trusted, leading to improved morale and stronger public image."
            }
        }
    },
    {
        "question": "Should we use AI to write product descriptions on our online store?",
        "options": {
            "A": {
                "text": "Fully replace writers with AI",
                "score_change": {"profit": 30, "public_opinion": -20, "morale": -25},
                "explanation": "Cost savings are clear, but former writers protest and media coverage is critical."
            },
            "B": {
                "text": "Use AI-generated drafts, but keep editors on staff",
                "score_change": {"profit": 15, "public_opinion": 5, "morale": 10},
                "explanation": "Maintains some creative control and jobs while increasing efficiency."
            },
            "C": {
                "text": "Keep human writers for all product descriptions",
                "score_change": {"profit": 0, "public_opinion": 0, "morale": 10},
                "explanation": "The human touch is preserved, but the company misses efficiency gains."
            }
        }
    },
    {
        "question": "Should we implement AI to predict which employees are likely to quit?",
        "options": {
            "A": {
                "text": "Yes, and use it to flag employees to management",
                "score_change": {"profit": 10, "public_opinion": -20, "morale": -30},
                "explanation": "Leaders feel more in control, but employees are outraged over perceived surveillance."
            },
            "B": {
                "text": "Yes, but only as an internal HR resource",
                "score_change": {"profit": 5, "public_opinion": 0, "morale": -10},
                "explanation": "Quietly improves retention planning, though workers feel slightly uneasy."
            },
            "C": {
                "text": "No, trust employees and address concerns openly",
                "score_change": {"profit": 0, "public_opinion": 10, "morale": 15},
                "explanation": "Improves workplace trust, but some preventable turnover occurs."
            }
        }
    },
    {
        "question": "Should we use generative AI to produce promotional materials?",
        "options": {
            "A": {
                "text": "Replace creative staff with AI entirely",
                "score_change": {"profit": 35, "public_opinion": -25, "morale": -40},
                "explanation": "Promotions are created quickly and cheaply, but creative staff revolt."
            },
            "B": {
                "text": "Use AI to support the creative team",
                "score_change": {"profit": 15, "public_opinion": 5, "morale": 5},
                "explanation": "Faster turnaround with fewer resources, and team feels supported, not replaced."
            },
            "C": {
                "text": "Keep human-only creative team",
                "score_change": {"profit": 0, "public_opinion": 0, "morale": 10},
                "explanation": "Work quality stays high, and staff remain loyal, but costs remain elevated."
            }
        }
    },
    {
        "question": "Should we outsource AI development to a third-party vendor?",
        "options": {
            "A": {
                "text": "Yes, cheapest offshore vendor",
                "score_change": {"profit": 25, "public_opinion": -15, "morale": -20},
                "explanation": "Saves money, but raises questions about data security and job loss."
            },
            "B": {
                "text": "Yes, a vetted domestic vendor with ethical oversight",
                "score_change": {"profit": 10, "public_opinion": 10, "morale": 5},
                "explanation": "More expensive, but employees and customers feel safer with the choice."
            },
            "C": {
                "text": "Build AI tools in-house",
                "score_change": {"profit": -10, "public_opinion": 5, "morale": 10},
                "explanation": "Costly and slow, but enhances technical expertise and trust in the company."
            }
        }
    },
    {
        "question": "Should we use AI to screen job applicants before human review?",
        "options": {
            "A": {
                "text": "Fully automate applicant screening",
                "score_change": {"profit": 20, "public_opinion": -20, "morale": -10},
                "explanation": "Hiring is faster and cheaper, but accusations of bias arise."
            },
            "B": {
                "text": "Use AI for initial filtering, followed by human oversight",
                "score_change": {"profit": 10, "public_opinion": 5, "morale": 0},
                "explanation": "Balanced approach improves speed while retaining some fairness checks."
            },
            "C": {
                "text": "Rely solely on human screening",
                "score_change": {"profit": -10, "public_opinion": 0, "morale": 5},
                "explanation": "Ensures fairness but slows hiring significantly."
            }
        }
    },
    {
        "question": "Should we use AI to generate employee performance evaluations?",
        "options": {
            "A": {
                "text": "Fully automate evaluations",
                "score_change": {"profit": 15, "public_opinion": -10, "morale": -30},
                "explanation": "Efficiency improves, but staff view evaluations as impersonal and inaccurate."
            },
            "B": {
                "text": "Use AI to support managers in making evaluations",
                "score_change": {"profit": 5, "public_opinion": 5, "morale": 0},
                "explanation": "Managers save time, and employees still feel seen."
            },
            "C": {
                "text": "Avoid AI and keep manager-led evaluations",
                "score_change": {"profit": -5, "public_opinion": 0, "morale": 10},
                "explanation": "Slower, but employees appreciate the human attention."
            }
        }
    },
    {
        "question": "Should we integrate AI in our call center operations?",
        "options": {
            "A": {
                "text": "Replace agents with AI voice assistants",
                "score_change": {"profit": 30, "public_opinion": -40, "morale": -50},
                "explanation": "Cost savings are significant, but customers and workers alike are unhappy."
            },
            "B": {
                "text": "Use AI to support human agents",
                "score_change": {"profit": 15, "public_opinion": 10, "morale": 5},
                "explanation": "Productivity rises without hurting the customer experience."
            },
            "C": {
                "text": "Stick with human agents",
                "score_change": {"profit": 0, "public_opinion": 0, "morale": 10},
                "explanation": "Customer service remains strong, but operating costs are higher."
            }
        }
    },
    {
        "question": "Should we implement facial recognition to track returning customers?",
        "options": {
            "A": {
                "text": "Yes, without consent",
                "score_change": {"profit": 20, "public_opinion": -50, "morale": -10},
                "explanation": "Effective marketing gains are overshadowed by public backlash and privacy concerns."
            },
            "B": {
                "text": "Yes, but ask for customer opt-in",
                "score_change": {"profit": 10, "public_opinion": 5, "morale": 0},
                "explanation": "Customers who opt in appreciate the personalized service."
            },
            "C": {
                "text": "Do not use facial recognition",
                "score_change": {"profit": 0, "public_opinion": 10, "morale": 5},
                "explanation": "Company avoids controversy and builds public trust."
            }
        }
    }
]
        
        self.questions += [
    {
        "question": "Should we use AI-driven scheduling software that optimizes labor costs by assigning fewer shifts?",
        "options": {
            "A": {
                "text": "Implement AI scheduling and reduce staff hours",
                "score_change": {"profit": 30, "public_opinion": -15, "morale": -40},
                "explanation": "You reduced staffing costs, improving profitability. However, employees faced unpredictable schedules and reduced income, leading to lower morale."
            },
            "B": {
                "text": "Use AI to suggest schedules, but allow manual overrides",
                "score_change": {"profit": 10, "public_opinion": 5, "morale": 5},
                "explanation": "You balanced automation with human oversight, earning respect from employees while still gaining operational efficiency."
            },
            "C": {
                "text": "Reject AI scheduling and keep manual shift planning",
                "score_change": {"profit": 0, "public_opinion": 0, "morale": 5},
                "explanation": "You maintained employee trust with consistent shifts, but missed potential savings in labor optimization."
            }
        }
    },
    {
        "question": "Should we use AI to analyze employees’ productivity and flag underperformers automatically?",
        "options": {
            "A": {
                "text": "Deploy AI monitoring with automated disciplinary action",
                "score_change": {"profit": 20, "public_opinion": -10, "morale": -50},
                "explanation": "Productivity improved slightly, but employees felt micromanaged and anxious, leading to morale issues and public scrutiny."
            },
            "B": {
                "text": "Use AI to inform managers privately, with discretion in handling",
                "score_change": {"profit": 10, "public_opinion": 5, "morale": 5},
                "explanation": "You maintained transparency while respecting employee privacy, creating a more supportive culture."
            },
            "C": {
                "text": "Avoid AI monitoring entirely",
                "score_change": {"profit": 0, "public_opinion": 0, "morale": 10},
                "explanation": "Employees appreciated the trust, though performance data was harder to track."
            }
        }
    },
    {
        "question": "Should we implement AI to manage our supply chain and automatically reorder inventory?",
        "options": {
            "A": {
                "text": "Fully automate inventory decisions with AI",
                "score_change": {"profit": 35, "public_opinion": 5, "morale": -15},
                "explanation": "Inventory costs dropped significantly, but employees in procurement roles felt displaced and undervalued."
            },
            "B": {
                "text": "Use AI to make suggestions but keep human control",
                "score_change": {"profit": 15, "public_opinion": 10, "morale": 5},
                "explanation": "You gained efficiency and boosted employee buy-in through collaborative decision-making."
            },
            "C": {
                "text": "Keep inventory decisions fully manual",
                "score_change": {"profit": -5, "public_opinion": 0, "morale": 5},
                "explanation": "You avoided disruption, but your processes remained slow and inefficient compared to competitors."
            }
        }
    },
    {
        "question": "Should we use AI to customize marketing emails based on customer behavior?",
        "options": {
            "A": {
                "text": "Fully personalize emails using AI behavioral data",
                "score_change": {"profit": 20, "public_opinion": -15, "morale": 0},
                "explanation": "Open and click rates improved, but some customers found the targeting invasive and reported discomfort."
            },
            "B": {
                "text": "Use anonymized behavior data to group customers into segments",
                "score_change": {"profit": 10, "public_opinion": 10, "morale": 0},
                "explanation": "You achieved moderate personalization while preserving privacy, boosting brand trust."
            },
            "C": {
                "text": "Avoid behavioral targeting altogether",
                "score_change": {"profit": -5, "public_opinion": 5, "morale": 0},
                "explanation": "You missed marketing efficiency but gained public appreciation for prioritizing privacy."
            }
        }
    },
    {
        "question": "Should we install AI-powered cameras to monitor employee-customer interactions for quality control?",
        "options": {
            "A": {
                "text": "Install AI cameras and issue automatic performance warnings",
                "score_change": {"profit": 20, "public_opinion": -20, "morale": -40},
                "explanation": "Customers noticed better service, but staff felt surveilled, and privacy advocates criticized the policy."
            },
            "B": {
                "text": "Use AI cameras for training and feedback, not discipline",
                "score_change": {"profit": 10, "public_opinion": 5, "morale": 10},
                "explanation": "Employees appreciated the focus on development, and customers responded positively to improved service."
            },
            "C": {
                "text": "Do not implement AI surveillance",
                "score_change": {"profit": 0, "public_opinion": 0, "morale": 10},
                "explanation": "You maintained a trusting environment, though opportunities to improve customer service were missed."
            }
        }
    },
    {
        "question": "Should we use AI to create deepfake-style virtual spokespeople for our advertisements?",
        "options": {
            "A": {
                "text": "Use realistic AI-generated avatars in ads without disclosure",
                "score_change": {"profit": 15, "public_opinion": -25, "morale": 0},
                "explanation": "The campaign attracted attention, but backlash arose over deceptive practices and transparency concerns."
            },
            "B": {
                "text": "Use AI avatars but clearly disclose their nature",
                "score_change": {"profit": 10, "public_opinion": 10, "morale": 0},
                "explanation": "Customers appreciated your creativity and honesty, leading to positive engagement."
            },
            "C": {
                "text": "Stick with traditional human actors",
                "score_change": {"profit": 0, "public_opinion": 0, "morale": 0},
                "explanation": "Your campaign was standard and safe, but lacked innovation that could have drawn attention."
            }
        }
    },
    {
        "question": "Should we introduce AI to monitor social media for brand mentions and automatically respond to customers?",
        "options": {
            "A": {
                "text": "Let AI fully manage responses without human input",
                "score_change": {"profit": 10, "public_opinion": -20, "morale": 0},
                "explanation": "Response time improved, but customers noticed robotic replies and felt ignored."
            },
            "B": {
                "text": "Use AI to flag and draft replies, but have humans approve them",
                "score_change": {"profit": 5, "public_opinion": 10, "morale": 0},
                "explanation": "You balanced speed with a human touch, improving customer satisfaction."
            },
            "C": {
                "text": "Continue relying solely on human social media managers",
                "score_change": {"profit": -5, "public_opinion": 0, "morale": 5},
                "explanation": "Social media interactions remained authentic, but you struggled to keep up with demand."
            }
        }
    },
    {
        "question": "Should we use AI to simulate potential store layouts for maximum efficiency?",
        "options": {
            "A": {
                "text": "Simulate and fully reconfigure store layout based on AI output",
                "score_change": {"profit": 25, "public_opinion": -10, "morale": -10},
                "explanation": "Efficiency improved, but both employees and customers took time to adapt, leading to frustration."
            },
            "B": {
                "text": "Test AI layout in one location before wider rollout",
                "score_change": {"profit": 10, "public_opinion": 5, "morale": 5},
                "explanation": "You reduced risk and involved employees in the process, creating buy-in."
            },
            "C": {
                "text": "Avoid using AI in physical store planning",
                "score_change": {"profit": 0, "public_opinion": 0, "morale": 0},
                "explanation": "You missed out on potential improvements but preserved familiarity and avoided pushback."
            }
        }
    },
    {
        "question": "Should we offer an AI-powered virtual assistant for employees to handle HR questions?",
        "options": {
            "A": {
                "text": "Fully replace HR frontline support with AI assistant",
                "score_change": {"profit": 15, "public_opinion": 0, "morale": -25},
                "explanation": "Costs dropped, but employees felt disconnected and unsupported in sensitive matters."
            },
            "B": {
                "text": "Introduce AI assistant but offer option to speak with HR staff",
                "score_change": {"profit": 5, "public_opinion": 0, "morale": 10},
                "explanation": "You improved efficiency while preserving employee trust through hybrid support."
            },
            "C": {
                "text": "Keep HR interactions human-only",
                "score_change": {"profit": 0, "public_opinion": 0, "morale": 5},
                "explanation": "Employees felt comfortable and respected, but HR staff struggled with high volumes of requests."
            }
        }
    },
    {
        "question": "Should we use AI sentiment analysis on employee emails to detect dissatisfaction early?",
        "options": {
            "A": {
                "text": "Scan all internal emails for sentiment without disclosure",
                "score_change": {"profit": 5, "public_opinion": -30, "morale": -50},
                "explanation": "You gathered insights but at the cost of employee trust and a major backlash once discovered."
            },
            "B": {
                "text": "Offer opt-in email analysis with incentives",
                "score_change": {"profit": 0, "public_opinion": 10, "morale": 5},
                "explanation": "You respected privacy and earned goodwill from employees who felt heard and supported."
            },
            "C": {
                "text": "Do not analyze internal communications",
                "score_change": {"profit": 0, "public_opinion": 0, "morale": 0},
                "explanation": "You maintained trust, but missed an opportunity to address hidden dissatisfaction proactively."
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
is calculated as a harmonic average of all 3 factors that measures how well you balanced them.

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
            font=("Helvetica", 15),
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
        
        # Check if any score went negative. Show lose screen if so.
        if self.profit <= 0 or self.public_opinion <= 0 or self.morale <= 0:
            # Calculate final score even if losing
            final_score = round(3 / (1/max(1, self.profit) + 1/max(1, self.public_opinion) + 1/max(1, self.morale)))
            # Remove messagebox and show the lose screen
            self.master.after(3000, lambda: self.show_end_screen("lose", final_score))
            return
            
        # Schedule the next question
        self.current_question += 1
        self.master.after(3000, self.load_question)
        
    def load_question(self):
        """Load a new question or finish the game."""
        if self.current_question >= len(self.questions):
            # Calculate final score
            final_score = round(3 / (1/self.profit + 1/self.public_opinion + 1/self.morale))
            # Show win screen instead of messagebox
            self.show_end_screen("win", final_score)
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
    
    def show_end_screen(self, result, final_score):
        """Show the win or lose screen with final score."""
        self.clear_screen()
        
        # Load the win or lose background image
        if result == "win":
            image_path = os.path.join("assets", "win.png")
        else:
            image_path = os.path.join("assets", "lose.png")
            
        self.end_bg_image = Image.open(image_path)
        # Resize the image to fit the window
        self.end_bg_image = self.end_bg_image.resize((800, 600), Image.LANCZOS)
        self.end_bg_photo = ImageTk.PhotoImage(self.end_bg_image)
        
        # Create a canvas to display the background image
        self.end_canvas = tk.Canvas(self.master, width=800, height=600)
        self.end_canvas.pack(fill="both", expand=True)
        self.end_canvas.create_image(0, 0, image=self.end_bg_photo, anchor="nw")
        
        # Create final score text in the middle of the screen
        self.end_canvas.create_text(
            400, 300,  # Center of the screen
            text=f"{final_score}",
            font=("Helvetica", 36, "bold"),
            fill="white",
            width=700,
            justify="center"
        )
        
        # Create text widgets for final KPI values (same positions as in game screen)
        self.end_canvas.create_text(
            180, 510,  # Position in the Profitability box at the bottom
            text=f"{self.profit}",
            font=("Helvetica", 24, "bold"),
            fill="white"
        )
        
        self.end_canvas.create_text(
            620, 510,  # Position in the Customer Satisfaction box at the bottom
            text=f"{self.public_opinion}",
            font=("Helvetica", 24, "bold"),
            fill="white"
        )
        
        self.end_canvas.create_text(
            390, 510,  # Position in the Employee Morale box at the bottom
            text=f"{self.morale}",
            font=("Helvetica", 24, "bold"),
            fill="white"
        )
        
        # Add a home button
        home_button = tk.Button(
            self.master,
            text="Return to Home",
            command=self.show_home_page,
            font=("Helvetica", 16),
            bg="#4CAF50",
            fg="black",
            padx=30,
            pady=5
        )
        home_button.pack(pady=5)
        home_button_window = self.end_canvas.create_window(400, 575, window=home_button)

if __name__ == "__main__":
    root = tk.Tk()
    game = GameUI(root)
    root.mainloop()