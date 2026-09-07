from candidate import (
    add_candidate,
    view_candidates,
    update_candidate,
    delete_candidate
)

from company import (
    add_company,
    view_companies,
    update_company,
    delete_company
)

from job import (
    add_job,
    view_jobs,
    update_job,
    delete_job
)

from application import (
    apply_for_job,
    view_applications,
    update_application,
    delete_application
)


while True:

    print("\n======================================")
    print("      ONLINE JOB APPLICATION SYSTEM")
    print("======================================")

    print("1. Add Candidate")
    print("2. View Candidates")
    print("3. Update Candidate")
    print("4. Delete Candidate")

    print("5. Add Company")
    print("6. View Companies")
    print("7. Update Company")
    print("8. Delete Company")

    print("9. Add Job")
    print("10. View Jobs")
    print("11. Update Job")
    print("12. Delete Job")

    print("13. Apply for Job")
    print("14. View Applications")
    print("15. Update Application Status")
    print("16. Delete Application")

    print("17. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_candidate()

    elif choice == "2":
        view_candidates()

    elif choice == "3":
        update_candidate()

    elif choice == "4":
        delete_candidate()

    elif choice == "5":
        add_company()

    elif choice == "6":
        view_companies()

    elif choice == "7":
        update_company()

    elif choice == "8":
        delete_company()

    elif choice == "9":
        add_job()

    elif choice == "10":
        view_jobs()

    elif choice == "11":
        update_job()

    elif choice == "12":
        delete_job()

    elif choice == "13":
        apply_for_job()

    elif choice == "14":
        view_applications()

    elif choice == "15":
        update_application()

    elif choice == "16":
        delete_application()

    elif choice == "17":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")