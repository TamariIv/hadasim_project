<template>
<div class="container">

    <!-- main page to view all users -->
    <div class="row">
        <div class="col-sm-10">
            <h1>Users</h1>
            <hr><br><br>
            <alert :message=message v-if="showMessage"></alert>
            <button
                type="button"
                class="btn btn-success btn-sm"
                @click="toggleAddUserModal">
                Add User
            </button>            
            <br><br>
            <table class="table table-hover">
                <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">First Name</th>
                    <th scope="col">Last Name</th>
                    <th scope="col">Email</th>
                    <th scope="col">Phone</th>
                    <th scope="col">Mobile</th>
                    <th scope="col">Adress</th>
                    <th scope="col">Birth Date</th>
                    <th scope="col">Vaccinated</th>
                    <th scope="col">Was Sick</th>

                    <th></th>
                </tr>
                </thead>
                <tbody>
                    <tr v-for="(user, index) in users" :key="index">
                    <td>{{ user.id }}</td>
                    <td>{{ user.first_name }}</td>
                    <td>{{ user.last_name }}</td>
                    <td>{{ user.email }}</td>
                    <td>{{ user.phone_number }}</td>
                    <td>{{ user.mobile_phone_number? user.mobile_phone_number : '-' }}</td>
                    <td>{{ user.city + ', ' + user.street + ' ' + user.building_number }}</td>
                    <td>{{ user.birth_date }}</td>
                    <td>{{ user.vaccines? 'Yes' : 'No' }}</td>
                    <td>{{ user.covid_positive_date? 'Yes' : 'No' }}</td>
                    <td>
                        <div class="btn-group" role="group">
                            <button
                            type="button"
                            class="btn btn-warning btn-sm"
                            @click="toggleEditUserModal(user)">
                            Update
                            </button>
                            <button type="button" class="btn btn-danger btn-sm">Delete</button>
                        </div>
                    </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- add new user modal -->
    <div
    ref="addUserModal"
    class="modal fade"
    :class="{ show: activeAddUserModal, 'd-block': activeAddUserModal }"
    tabindex="-1"
    role="dialog">
    <div class="modal-dialog" role="document">
    <div class="modal-content">
        <div class="modal-header">
        <h5 class="modal-title">Add a new user</h5>
        <button
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
            @click="toggleAddUserModal">
            <span aria-hidden="true">&times;</span>
        </button>
        </div>
        <div class="modal-body">
        <form>
            <div class="mb-3">
                <label for="addUserId" class="form-label">ID:</label>
                <input
                    type="text"
                    class="form-control"
                    id="addUserId"
                    v-model="addUserForm.id"
                    placeholder="Enter ID">
            </div>

            <div class="mb-3">
                <label for="addUserFirstName" class="form-label">First Name:</label>
                <input
                    type="text"
                    class="form-control"
                    id="addUserFirstName"
                    v-model="addUserForm.first_name"
                    placeholder="Enter first name">
            </div>

            <div class="mb-3">
                <label for="addUserLastName" class="form-label">Last Name:</label>
                <input
                    type="text"
                    class="form-control"
                    id="addUserAuthor"
                    v-model="addUserForm.last_name"
                    placeholder="Enter last name">
            </div>

            <div class="mb-3">
                <label for="addUserEmail" class="form-label">Email:</label>
                <input
                    type="text"
                    class="form-control"
                    id="addUserEmail"
                    v-model="addUserForm.email"
                    placeholder="Enter Email">
            </div>

            <div class="mb-3">
                <label for="addUserCity" class="form-label">City:</label>
                <input
                    type="text"
                    class="form-control"
                    id="addUserCity"
                    v-model="addUserForm.city"
                    placeholder="Enter City">
            </div>
            
            <div class="mb-3">
                <label for="addUserStreet" class="form-label">Street:</label>
                <input
                    type="text"
                    class="form-control"
                    id="addUserStreet"
                    v-model="addUserForm.street"
                    placeholder="Enter Street">
            </div> 

            <div class="mb-3">
                <label for="addUserBuildingNumber" class="form-label">Building Number:</label>
                <input
                    type="text"
                    class="form-control"
                    id="addUserBuildingNumber"
                    v-model="addUserForm.building_number"
                    placeholder="Enter Building Number">
            </div>

            <div class="mb-3">
                <label for="addUserBirthDate" class="form-label">Birth Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="addUserBirthDate"
                    v-model="addUserForm.birth_date">
            </div>

            <div class="mb-3">
                <label for="addUserPhoneNumber" class="form-label">Phone Number:</label>
                <input
                    type="tel"
                    class="form-control"
                    id="addUserPhoneNumber"
                    v-model="addUserForm.phone_number"
                    placeholder="Enter Phone Number">
            </div>

            <div class="mb-3">
                <label for="addUserMobilePhoneNumber" class="form-label">Mobile Phone Number:</label>
                <input
                    type="tel"
                    class="form-control"
                    id="addUserMobilePhoneNumber"
                    v-model="addUserForm.mobile_phone_number"
                    placeholder="Enter Mobile Phone Number">
            </div>

            <div class="mb-3">
                <label for="addUserCovidPositiveDate" class="form-label">COVID Positive Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="addUserCovidPositiveDate"
                    v-model="addUserForm.covid_positive_date">
            </div>

            <div class="mb-3">
                <label for="addUserCovidRecoveryDate" class="form-label">COVID Recovery Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="addUserCovidRecoveryDate"
                    v-model="addUserForm.covid_recovery_date">
            </div>

            <h3>Vaccine 1</h3>
            <div class="mb-3">
                <label for="addUserVaccine1Provider" class="form-label">Vaccine Provider:</label>
                <input
                    type="text"
                    class="form-control"
                    id="addUserVaccine1Provider"
                    v-model="addUserForm.vaccine_1_provider">
            </div>
            <div class="mb-3">
                <label for="addUserVaccine1Date" class="form-label">Vaccine Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="addUserVaccine1Date"
                    v-model="addUserForm.vaccine_1_date_taken">
            </div>

            <h3>Vaccine 2</h3>
            <div class="mb-3">
                <label for="addUserVaccine2Provider" class="form-label">Vaccine Provider:</label>
                <input
                    type="text"
                    class="form-control"
                    id="addUserVaccine2Provider"
                    v-model="addUserForm.vaccine_2_provider">
            </div>
            <div class="mb-3">
                <label for="addUserVaccine2Date" class="form-label">Vaccine Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="addUserVaccine2Date"
                    v-model="addUserForm.vaccine_2_date_taken">
            </div>

            <h3>Vaccine 3</h3>
            <div class="mb-3">
                <label for="addUserVaccine3Provider" class="form-label">Vaccine Provider:</label>
                <input
                    type="text"
                    class="form-control"
                    id="addUserVaccine3Provider"
                    v-model="addUserForm.vaccine_3_provider">
            </div>
            <div class="mb-3">
                <label for="addUserVaccine3Date" class="form-label">Vaccine Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="addUserVaccine3Date"
                    v-model="addUserForm.vaccine_3_date_taken">
            </div>
            
            <h3>Vaccine 4</h3>
            <div class="mb-3">
                <label for="addUserVaccine4Provider" class="form-label">Vaccine Provider:</label>
                <input
                    type="text"
                    class="form-control"
                    id="addUserVaccine4Provider"
                    v-model="addUserForm.vaccine_4_provider">
            </div>
            <div class="mb-3">
                <label for="addUserVaccine4Date" class="form-label">Vaccine Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="addUserVaccine4Date"
                    v-model="addUserForm.vaccine_4_date_taken">
            </div>

            <div class="btn-group" role="group">
                <button
                    type="button"
                    class="btn btn-primary btn-sm"
                    @click="handleAddSubmit">
                    Submit
                </button>
                <button
                    type="button"
                    class="btn btn-danger btn-sm"
                    @click="handleAddReset">
                    Reset
                </button>
            </div>
        </form>
        </div>
    </div>
    </div>
    </div>
    <div v-if="activeAddUserModal" class="modal-backdrop fade show"></div>

    <!-- edit user modal -->
    <div
    ref="editUserModal"
    class="modal fade"
    :class="{ show: activeEditUserModal, 'd-block': activeEditUserModal }"
    tabindex="-1"
    role="dialog">
    <div class="modal-dialog" role="document">
    <div class="modal-content">
        <div class="modal-header">
        <h5 class="modal-title">Update</h5>
        <button
            type="button"
            class="close"
            data-dismiss="modal"
            aria-label="Close"
            @click="toggleEditUserModal">
            <span aria-hidden="true">&times;</span>
        </button>
        </div>
        <div class="modal-body">
        <form>
            <div class="mb-3">
                <label for="editUserId" class="form-label">ID:</label>
                <input
                    type="text"
                    class="form-control"
                    id="editUserId"
                    v-model="editUserForm.id"
                    placeholder="Enter ID">
            </div>

            <div class="mb-3">
                <label for="editUserFirstName" class="form-label">First Name:</label>
                <input
                    type="text"
                    class="form-control"
                    id="editUserFirstName"
                    v-model="editUserForm.first_name"
                    placeholder="Enter first name">
            </div>

            <div class="mb-3">
                <label for="editUserLastName" class="form-label">Last Name:</label>
                <input
                    type="text"
                    class="form-control"
                    id="editUserAuthor"
                    v-model="editUserForm.last_name"
                    placeholder="Enter last name">
            </div>

            <div class="mb-3">
                <label for="editUserEmail" class="form-label">Email:</label>
                <input
                    type="text"
                    class="form-control"
                    id="editUserEmail"
                    v-model="editUserForm.email"
                    placeholder="Enter Email">
            </div>

            <div class="mb-3">
                <label for="editUserCity" class="form-label">City:</label>
                <input
                    type="text"
                    class="form-control"
                    id="editUserCity"
                    v-model="editUserForm.city"
                    placeholder="Enter City">
            </div>
            
            <div class="mb-3">
                <label for="editUserStreet" class="form-label">Street:</label>
                <input
                    type="text"
                    class="form-control"
                    id="editUserStreet"
                    v-model="editUserForm.street"
                    placeholder="Enter Street">
            </div> 

            <div class="mb-3">
                <label for="editUserBuildingNumber" class="form-label">Building Number:</label>
                <input
                    type="text"
                    class="form-control"
                    id="editUserBuildingNumber"
                    v-model="editUserForm.building_number"
                    placeholder="Enter Building Number">
            </div>

            <div class="mb-3">
                <label for="editUserBirthDate" class="form-label">Birth Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="editUserBirthDate"
                    v-model="editUserForm.birth_date">
            </div>

            <div class="mb-3">
                <label for="editUserPhoneNumber" class="form-label">Phone Number:</label>
                <input
                    type="tel"
                    class="form-control"
                    id="editUserPhoneNumber"
                    v-model="editUserForm.phone_number"
                    placeholder="Enter Phone Number">
            </div>

            <div class="mb-3">
                <label for="editUserMobilePhoneNumber" class="form-label">Mobile Phone Number:</label>
                <input
                    type="tel"
                    class="form-control"
                    id="editUserMobilePhoneNumber"
                    v-model="editUserForm.mobile_phone_number"
                    placeholder="Enter Mobile Phone Number">
            </div>

            <div class="mb-3">
                <label for="editUserCovidPositiveDate" class="form-label">COVID Positive Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="editUserCovidPositiveDate"
                    v-model="editUserForm.covid_positive_date">
            </div>

            <div class="mb-3">
                <label for="editUserCovidRecoveryDate" class="form-label">COVID Recovery Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="editUserCovidRecoveryDate"
                    v-model="editUserForm.covid_recovery_date">
            </div>

            <h3>Vaccine 1</h3>
            <div class="mb-3">
                <label for="editUserVaccine1Provider" class="form-label">Vaccine Provider:</label>
                <input
                    type="text"
                    class="form-control"
                    id="editUserVaccine1Provider"
                    v-model="editUserForm.vaccine_1_provider">
            </div>
            <div class="mb-3">
                <label for="editUserVaccine1Date" class="form-label">Vaccine Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="editUserVaccine1Date"
                    v-model="editUserForm.vaccine_1_date_taken">
            </div>

            <h3>Vaccine 2</h3>
            <div class="mb-3">
                <label for="editUserVaccine2Provider" class="form-label">Vaccine Provider:</label>
                <input
                    type="text"
                    class="form-control"
                    id="editUserVaccine2Provider"
                    v-model="editUserForm.vaccine_2_provider">
            </div>
            <div class="mb-3">
                <label for="editUserVaccine2Date" class="form-label">Vaccine Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="editUserVaccine2Date"
                    v-model="editUserForm.vaccine_2_date_taken">
            </div>

            <h3>Vaccine 3</h3>
            <div class="mb-3">
                <label for="editUserVaccine3Provider" class="form-label">Vaccine Provider:</label>
                <input
                    type="text"
                    class="form-control"
                    id="editUserVaccine3Provider"
                    v-model="editUserForm.vaccine_3_provider">
            </div>
            <div class="mb-3">
                <label for="editUserVaccine3Date" class="form-label">Vaccine Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="editUserVaccine3Date"
                    v-model="editUserForm.vaccine_3_date_taken">
            </div>
            
            <h3>Vaccine 4</h3>
            <div class="mb-3">
                <label for="editUserVaccine4Provider" class="form-label">Vaccine Provider:</label>
                <input
                    type="text"
                    class="form-control"
                    id="editUserVaccine4Provider"
                    v-model="editUserForm.vaccine_4_provider">
            </div>
            <div class="mb-3">
                <label for="editUserVaccine4Date" class="form-label">Vaccine Date:</label>
                <input
                    type="date"
                    class="form-control"
                    id="editUserVaccine4Date"
                    v-model="editUserForm.vaccine_4_date_taken">
            </div>

            <div class="btn-group" role="group">
            <button
                type="button"
                class="btn btn-primary btn-sm"
                @click="handleEditSubmit">
                Submit
            </button>
            <button
                type="button"
                class="btn btn-danger btn-sm"
                @click="handleEditCancel">
                Cancel
            </button>
            </div>
        </form>
        </div>
    </div>
    </div>
    </div>
    <div v-if="activeEditUserModal" class="modal-backdrop fade show"></div>
</div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
    data() {
        return {
            activeAddUserModal: false,
            addUserForm: {
                id: '',
                first_name: '',
                last_name: '',
                email: '',
                city: '',
                street: '',
                building_number: '',
                birth_date: '',
                phone_number: '',
                mobile_phone_number: '',
                vaccine_1_provider: '',
                vaccine_1_date_taken: '',
                vaccine_2_provider: '',
                vaccine_2_date_taken: '',
                vaccine_3_provider: '',
                vaccine_3_date_taken: '',
                vaccine_4_provider: '',
                vaccine_4_date_taken: '',
                covid_positive_date: '',
                covid_recovery_date: ''
            },
            activeEditUserModal: false,
            editUserForm: {
                id: '',
                first_name: '',
                last_name: '',
                email: '',
                city: '',
                street: '',
                building_number: '',
                birth_date: '',
                phone_number: '',
                mobile_phone_number: '',
                vaccine_1_provider: '',
                vaccine_1_date_taken: '',
                vaccine_2_provider: '',
                vaccine_2_date_taken: '',
                vaccine_3_provider: '',
                vaccine_3_date_taken: '',
                vaccine_4_provider: '',
                vaccine_4_date_taken: '',
                covid_positive_date: '',
                covid_recovery_date: ''
            },
            users: [],
            message: '',
            showMessage: false,
        };
    },
    components: {
        alert: Alert,
    },
    methods: {
        addUser(payload) {
            const path = 'http://localhost:5001/users';
            axios.post(path, payload)
                .then(() => {
                    this.getUsers();
                    this.message = 'User added successfully!';
                    this.showMessage = true;
                })
                .catch((error) => {
                    console.log(error);
                    this.getUsers();
                });
        },
        getUsers() {
            const path = 'http://localhost:5001/users';
            axios.get(path)
                .then((res) => {
                    this.users = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
        handleAddReset() {
            this.initForm();
        },
        handleAddSubmit() {
            this.toggleAddUserModal();
            const payload = {
                id: this.addUserForm.id,
                first_name: this.addUserForm.first_name,
                last_name: this.addUserForm.last_name,
                email: this.addUserForm.email,
                city: this.addUserForm.city,
                street: this.addUserForm.street,
                building_number: this.addUserForm.building_number,
                birth_date: this.addUserForm.birth_date,
                phone_number: this.addUserForm.phone_number,
                mobile_phone_number: this.addUserForm.mobile_phone_number,
                vaccines: [
                    {date_taken: this.addUserForm.vaccine_1_date_taken, provider: this.addUserForm.vaccine_1_provider},
                    {date_taken: this.addUserForm.vaccine_2_date_taken, provider: this.addUserForm.vaccine_2_provider},
                    {date_taken: this.addUserForm.vaccine_3_date_taken, provider: this.addUserForm.vaccine_3_provider},
                    {date_taken: this.addUserForm.vaccine_4_date_taken, provider: this.addUserForm.vaccine_4_provider}
                ],
                covid_positive_date: this.addUserForm.covid_positive_date,
                covid_recovery_date: this.addUserForm.covid_recovery_date
            };
            this.addUser(payload);
            this.initForm();
        },
        initForm() {
            this.addUserForm.id = '';
            this.addUserForm.first_name = '';
            this.addUserForm.last_name = '';
            this.addUserForm.email = '';
            this.addUserForm.city = '';
            this.addUserForm.street = '';
            this.addUserForm.building_number = '';
            this.addUserForm.birth_date = '';
            this.addUserForm.phone_number = '';
            this.addUserForm.mobile_phone_number = '';
            this.addUserForm.vaccine_1_provider = '',
            this.addUserForm.vaccine_1_date_taken = '',
            this.addUserForm.vaccine_2_provider = '',
            this.addUserForm.vaccine_2_date_taken = '',
            this.addUserForm.vaccine_3_provider = '',
            this.addUserForm.vaccine_3_date_taken = '',
            this.addUserForm.vaccine_4_provider = '',
            this.addUserForm.vaccine_4_date_taken = '',            
            this.addUserForm.covid_positive_date = '';
            this.addUserForm.covid_recovery_date = '';

            this.editUserForm.id = '';
            this.editUserForm.first_name = '';
            this.editUserForm.last_name = '';
            this.editUserForm.email = '';
            this.editUserForm.city = '';
            this.editUserForm.street = '';
            this.editUserForm.building_number = '';
            this.editUserForm.birth_date = '';
            this.editUserForm.phone_number = '';
            this.editUserForm.mobile_phone_number = '';
            this.editUserForm.vaccine_1_provider = '',
            this.editUserForm.vaccine_1_date_taken = '',
            this.editUserForm.vaccine_2_provider = '',
            this.editUserForm.vaccine_2_date_taken = '',
            this.editUserForm.vaccine_3_provider = '',
            this.editUserForm.vaccine_3_date_taken = '',
            this.editUserForm.vaccine_4_provider = '',
            this.editUserForm.vaccine_4_date_taken = '',            
            this.editUserForm.covid_positive_date = '';
            this.editUserForm.covid_recovery_date = '';
        },
        toggleAddUserModal() {
            const body = document.querySelector('body');
            this.activeAddUserModal = !this.activeAddUserModal;
            if (this.activeAddUserModal) {
                body.classList.add('modal-open');
            } else {
                body.classList.remove('modal-open');
            }
        },
        handleEditCancel() {
            this.toggleEditBookModal(null);
            this.initForm();
            this.getBooks();
        },
        updateUser(payload, userID) {
            const path = `http://localhost:5001/users/${userID}`;
            axios.put(path, payload)
                .then(() => {
                    this.getUsers();
                    this.message = 'User updated!';
                    this.showMessage = true;
                })
                .catch((error) => {
                    console.error(error);
                    this.getUsers();
                });
        },
        handleEditSubmit() {
            this.toggleEditUserModal(null);
            const payload = {
                id: this.addUserForm.id,
                first_name: this.addUserForm.first_name,
                last_name: this.addUserForm.last_name,
                email: this.addUserForm.email,
                city: this.addUserForm.city,
                street: this.addUserForm.street,
                building_number: this.addUserForm.building_number,
                birth_date: this.addUserForm.birth_date,
                phone_number: this.addUserForm.phone_number,
                mobile_phone_number: this.addUserForm.mobile_phone_number,
                vaccines: [
                    {date_taken: this.addUserForm.vaccine_1_date_taken, provider: this.addUserForm.vaccine_1_provider},
                    {date_taken: this.addUserForm.vaccine_2_date_taken, provider: this.addUserForm.vaccine_2_provider},
                    {date_taken: this.addUserForm.vaccine_3_date_taken, provider: this.addUserForm.vaccine_3_provider},
                    {date_taken: this.addUserForm.vaccine_4_date_taken, provider: this.addUserForm.vaccine_4_provider}
                ],
                covid_positive_date: this.addUserForm.covid_positive_date,
                covid_recovery_date: this.addUserForm.covid_recovery_date
            };
            this.updateUser(payload, this.editUserForm.id);
        },
        toggleEditUserModal(user) {
            if (user) {
                this.editUserForm = user;
            }
            const body = document.querySelector('body');
            this.activeEditUserModal = !this.activeEditUserModal;
            if (this.activeEditUserModal) {
                body.classList.add('modal-open');
            } else{
                body.classList.remove('modal-open');
            }
        },
    },
    created() {
        this.getUsers();
    },
};
</script>